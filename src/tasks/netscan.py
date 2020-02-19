import netifaces


def run_faces():
    faces=[]
    for iface  in netifaces.interfaces():
        if iface == 'lo' or iface.startswith('vbox'):
            continue
        mac = netifaces.ifaddresses(iface)[netifaces.AF_LINK][0]['addr']
        if(mac):
            try:
                ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
                faces.append({"ip":ip,"mac":mac})
            except KeyError:
                continue
    return faces
