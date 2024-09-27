from django.shortcuts import render


def main(request):
    
    return render(request, '1.html')

def submit(request):
    if request.method == "POST":
        print("Form Data Received:", request.POST)  # Log all POST data

        try:
            # Extract POST data
            
            tstring = request.POST.get('tstring')
            clawstring=request.POST.get('rstring')
            Rstring=request.POST.get('Rstring')
            
            print("Received tstring:", clawstring)  # Log tstring value
            # Look for an existing entry based on a unique identifier (sprno in this case)
            en = Table.objects.filter(toa=spp).first()

            if en:
                if btype:
                    en.btype = btype
                   
                if flb1:
                    en.flb1 = int(flb1)
                if flb2:
                    en.flb2 = int(flb2)
                if flb3:
                    en.flb3 = int(flb3)
                if flb4:
                    en.flb4 = int(flb4)
                if slb1:
                    en.slb1 = int(slb1)
                if slb2:
                    en.slb2 = int(slb2)
                if slb3:
                    en.slb3 = int(slb3)
                if slb4:
                    en.slb4 = int(slb4)
                if flnb1:
                    en.flnb1 = int(flnb1)
                if flnb2:
                    en.flnb2 = int(flnb2)
                if flnb3:
                    en.flnb3 = int(flnb3)
                if flnb4:
                    en.flnb4 = int(flnb4)
                if slnb1:
                    en.slnb1 = int(slnb1)
                if slnb2:
                    en.slnb2 = int(slnb2)
                if slnb3:
                    en.slnb3 = int(slnb3)
                if slnb4:
                    en.slnb4 = int(slnb4)
                if sprd:
                    en.sprd = sprd
                if Dooc:
                    en.Dooc = Dooc
                if Priority:
                    en.Priority = Priority
                if memono:
                    en.memono = memono
                if project:
                    en.project = project
                if subsystem:
                    en.subsystem = subsystem
                if asto:
                    en.Assigned_to= asto
                if iby:
                    en.Initiated_by = iby
                if aby:
                    en.Approved_by = aby
                if sprno:
                    en.sprno=sprno
                if pct:
                    en.pct=pct
                if pcd:
                    en.pcd=pcd
                if tstring:
                    print("Received tstring:", tstring)

                    en.tstring=tstring
                if clawstring:
                    en.clawstring=clawstring
                    print("Received clawstring:", clawstring)
                if Rstring:
                    en.Rstring=Rstring


                
                en.save()
            else:
                # If no entry exists, create a new one
                en = Table(
                    
                    btype=btype,
                    spp=spp,
                    flb1=int(flb1) if flb1 else None,
                    flb2=int(flb2) if flb2 else None,
                    flb3=int(flb3) if flb3 else None,
                    flb4=int(flb4) if flb4 else None,
                    slb1=int(slb1) if slb1 else None,
                    slb2=int(slb2) if slb2 else None,
                    slb3=int(slb3) if slb3 else None,
                    slb4=int(slb4) if slb4 else None,
                    flnb1=int(flnb1) if flnb1 else None,
                    flnb2=int(flnb2) if flnb2 else None,
                    flnb3=int(flnb3) if flnb3 else None,
                    flnb4=int(flnb4) if flnb4 else None,
                    slnb1=int(slnb1) if slnb1 else None,
                    slnb2=int(slnb2) if slnb2 else None,
                    slnb3=int(slnb3) if slnb3 else None,
                    slnb4=int(slnb4) if slnb4 else None,
                    sprd=sprd,
                    Dooc=Dooc,
                    Priority=Priority,
                    sprno=sprno,
                    memono=memono,
                    project=project,
                    subsystem=subsystem,
                    Assigned_to=asto,
                    Initiated_by=iby,
                    Approved_by=aby,
                    pcd=pcd,
                    pct=pct,
                    tstring=tstring,
                    clawstring=clawstring,
                    Rstring=Rstring

                )
            en.save()
            print("tstrings value:", tstring)
            return redirect(next_url)
        except Exception as e:
            print("Error saving data:", e)
        return HttpResponseRedirect("")
    return redirect('Buildinfo')