from django.shortcuts import render


def main(request):
    
    return render(request, '1.html')

def submit(request):
    if request.method == "POST":
        print("Form Data Received:", request.POST)  # Log all POST data

        try:
            # Extract POST data
            
            toa = request.POST.get('toa')
            
            
            print("Received tstring:", clawstring)  # Log tstring value
            # Look for an existing entry based on a unique identifier (sprno in this case)
            en = Table.objects.filter(toa=toa).first()

            if en:
                if toa:
                    en.toa = toa
                   
                

                
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