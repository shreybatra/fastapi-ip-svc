import socket
from fastapi import FastAPI

app = FastAPI()


def get_all_ips() -> dict[str, str]:
    ips = {}
    for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
        addr = info[4]
        ip = addr[0] if isinstance(addr[0], str) else None
        if ip and not ip.startswith("127."):
            ips[f"iface_{len(ips)}"] = ip
    return ips


@app.get("/my-ip")
def my_ip():
    return {"hostname": socket.gethostname(), "interfaces": get_all_ips()}
