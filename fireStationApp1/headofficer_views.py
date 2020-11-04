from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Staff, Station, Vehicle_type, Designation, Vehicle, Reporter, Complaint, Act


def admin_home(request):
    return render(request, "headOfficerTemplate/home_content.html")

def add_staff(request):
    stations=Station.objects.all()
    designations=Designation.objects.all()
    return render(request, "headOfficerTemplate/add_staff.html",{"stations":stations,"designations":designations })

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        try:
            name=request.POST.get("fullname")
            gender=request.POST.get("gender")
            dob=request.POST.get("dob")
            contact=request.POST.get("contact")
            doj=request.POST.get("doj")
            salary=request.POST.get("salary")
            station_id=request.POST.get("station_id")
            station_obj = Station.objects.get(id=station_id)
            station_id = station_obj
            designation_id=request.POST.get("designation_id")
            designation_obj = Designation.objects.get(id=designation_id)
            designation_id = designation_obj

            Staff.objects.create(name=name,gender=gender,dob=dob,contact=contact,doj=doj,salary=salary,station_id=station_id,designation_id=designation_id)
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/add_staff")

def add_station(request):
    return render(request, "headOfficerTemplate/add_station.html")

def add_station_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        try:
            address=request.POST.get("address")
            contact=request.POST.get("contact")

            Station.objects.create(address=address,contact=contact)
            messages.success(request,"Successfully Added Station")
            return HttpResponseRedirect("/add_station")
        except:
            messages.error(request,"Failed to Add Station")
            return HttpResponseRedirect("/add_station")

def add_vehicle_type(request):
    return render(request, "headOfficerTemplate/add_vehicle_type.html")

def add_vehicle_type_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        try:
            name=request.POST.get("name")
            mobile=request.POST.get("mobile")
            water_capacity=request.POST.get("water_capacity")

            Vehicle_type.objects.create(name=name,mobile=mobile,water_capacity=water_capacity)
            messages.success(request,"Successfully Added Vehicle Type")
            return HttpResponseRedirect("/add_vehicle_type")
        except:
            messages.error(request,"Failed to Add Vehicle Type")
            return HttpResponseRedirect("/add_vehicle_type")

def add_vehicle(request):
    stations = Station.objects.all()
    vehicle_types = Vehicle_type.objects.all()
    return render(request, "headOfficerTemplate/add_vehicle.html",{"stations":stations,"vehicle_types":vehicle_types })

def add_vehicle_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        try:
            vehicle_number=request.POST.get("vehicle_number")
            purchase_date=request.POST.get("purchase_date")
            status=request.POST.get("status")
            vehicle_type_id=request.POST.get("vehicle_type_id")
            vehicle_type_obj = Vehicle_type.objects.get(id=vehicle_type_id)
            vehicle_type_id=vehicle_type_obj
            station_id=request.POST.get("station_id")
            station_obj = Station.objects.get(id=station_id)
            station_id = station_obj

            Vehicle.objects.create(vehicle_number=vehicle_number,purchase_date=purchase_date,status=status,vehicle_type_id=vehicle_type_id,station_id=station_id)
            messages.success(request,"Successfully Added Vehicle")
            return HttpResponseRedirect("/add_vehicle")
        except:
            messages.error(request,"Failed to Add Vehicle")
            return HttpResponseRedirect("/add_vehicle")

def manage_staff(request):
    staffs=Staff.objects.all()
    return render(request, "headOfficerTemplate/manage_staff.html",{"staffs":staffs})

def edit_staff(request,staff_id):
    staff=Staff.objects.get(id=staff_id)
    stations = Station.objects.all()
    designations = Designation.objects.all()
    return render(request,"headOfficerTemplate/edit_staff.html",{"staff":staff,"stations":stations,"designations":designations})

def edit_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        try:
            staff_id = request.POST.get("staff_id")
            name=request.POST.get("fullname")
            gender=request.POST.get("gender")
            dob=request.POST.get("dob")
            contact=request.POST.get("contact")
            doj=request.POST.get("doj")
            salary=request.POST.get("salary")
            station_id=request.POST.get("station_id")
            station_obj = Station.objects.get(id=station_id)
            station_id = station_obj
            designation_id=request.POST.get("designation_id")
            designation_obj = Designation.objects.get(id=designation_id)
            designation_id = designation_obj

            staff=Staff.objects.get(id=staff_id)
            staff.name=name
            staff.gender=gender
            staff.dob=dob
            staff.contact=contact
            staff.doj=doj
            staff.salary=salary
            staff.station_id=station_id
            staff.designation_id=designation_id
            staff.save()

            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect("/edit_staff/"+staff_id)
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect("/edit_staff/"+staff_id)

def manage_station(request):
    stations=Station.objects.all()
    return render(request, "headOfficerTemplate/manage_station.html",{"stations":stations})

def edit_station(request,station_id):
    station=Station.objects.get(id=station_id)
    return render(request,"headOfficerTemplate/edit_station.html",{"station":station})

def edit_station_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        try:
            station_id = request.POST.get("station_id")
            address=request.POST.get("address")
            contact=request.POST.get("contact")

            station=Station.objects.get(id=station_id)
            station.address=address
            station.contact=contact
            station.save()

            messages.success(request,"Successfully Edited Station")
            return HttpResponseRedirect("/edit_station/"+station_id)
        except:
            messages.error(request,"Failed to Edit Station")
            return HttpResponseRedirect("/edit_staff/"+station_id)

def manage_vehicle_type(request):
    vehicle_types=Vehicle_type.objects.all()
    return render(request, "headOfficerTemplate/manage_vehicle_type.html",{"vehicle_types":vehicle_types})

def edit_vehicle_type(request,vehicle_type_id):
    vehicle_type=Vehicle_type.objects.get(id=vehicle_type_id)
    return render(request,"headOfficerTemplate/edit_vehicle_type.html",{"vehicle_type":vehicle_type})

def edit_vehicle_type_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        try:
            vehicle_type_id = request.POST.get("vehicle_type_id")
            name=request.POST.get("name")
            mobile=request.POST.get("mobile")
            water_capacity=request.POST.get("water_capacity")

            vehicle_type=Vehicle_type.objects.get(id=vehicle_type_id)
            vehicle_type.name=name
            vehicle_type.mobile=mobile
            vehicle_type.water_capacity=water_capacity
            vehicle_type.save()

            messages.success(request,"Successfully Edited Vehicle Type")
            return HttpResponseRedirect("/edit_vehicle_type/"+vehicle_type_id)
        except:
            messages.error(request,"Failed to Edit Vehicle Type")
            return HttpResponseRedirect("/edit_vehicle_type/"+vehicle_type_id)

def manage_vehicle(request):
    vehicles=Vehicle.objects.all()
    return render(request, "headOfficerTemplate/manage_vehicle.html",{"vehicles":vehicles})

def edit_vehicle(request,vehicle_id):
    vehicle=Vehicle.objects.get(id=vehicle_id)
    stations = Station.objects.all()
    vehicle_types = Vehicle_type.objects.all()
    return render(request,"headOfficerTemplate/edit_vehicle.html",{"vehicle":vehicle,"stations":stations,"vehicle_types":vehicle_types})

def edit_vehicle_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        try:
            vehicle_id = request.POST.get("vehicle_id")
            vehicle_number=request.POST.get("vehicle_number")
            purchase_date=request.POST.get("purchase_date")
            status=request.POST.get("status")
            station_id=request.POST.get("station_id")
            station_obj = Station.objects.get(id=station_id)
            station_id = station_obj
            vehicle_type_id=request.POST.get("vehicle_type_id")
            vehicle_type_obj = Vehicle_type.objects.get(id=vehicle_type_id)
            vehicle_type_id = vehicle_type_obj

            vehicle=Vehicle.objects.get(id=vehicle_id)
            vehicle.vehicle_number=vehicle_number
            vehicle.purchase_date=purchase_date
            vehicle.status=status
            vehicle.station_id=station_id
            vehicle.vehicle_type_id=vehicle_type_id
            vehicle.save()

            messages.success(request,"Successfully Edited Vehicle")
            return HttpResponseRedirect("/edit_vehicle/"+vehicle_id)
        except:
            messages.error(request,"Failed to Edit Vehicle")
            return HttpResponseRedirect("/edit_vehicle/"+vehicle_id)

def make_report(request):
    reporters=Reporter.objects.all()
    return render(request, "headOfficerTemplate/make_report.html",{"reporters":reporters})

def make_report_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:

        description=request.POST.get("description")
        pin=request.POST.get("pin")
        street=request.POST.get("street")
        city=request.POST.get("city")
        state=request.POST.get("state")

        Complaint.objects.create(description=description,pin=pin,street=street,city=city,state=state)
        messages.success(request,"Successfully Made Report")
        return HttpResponseRedirect("/make_report")



def add_complainer(request):
    return render(request, "headOfficerTemplate/add_complainer.html")

def add_complainer_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        try:
            name=request.POST.get("name")
            email=request.POST.get("email")
            contact=request.POST.get("contact")
            reporting_date=request.POST.get("reporting_date")

            Reporter.objects.create(name=name,email=email,contact=contact,reporting_date=reporting_date)
            messages.success(request,"Successfully Added Complainer")
            return HttpResponseRedirect("/add_complainer")
        except:
            messages.error(request,"Failed to Add Complainer")
            return HttpResponseRedirect("/add_complainer")

def add_action(request):
    vehicles=Vehicle.objects.all()
    staffs=Staff.objects.all()
    complaints=Complaint.objects.all()
    return render(request, "headOfficerTemplate/add_action.html",{"vehicles":vehicles,"staffs":staffs,"complaints":complaints})

def add_action_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:

        status=request.POST.get("status")
        description=request.POST.get("description")

        Act.objects.create(status=status,description=description)
        messages.success(request,"Successfully Added Action")
        return HttpResponseRedirect("/add_action")
