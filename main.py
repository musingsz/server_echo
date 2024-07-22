from fastapi import FastAPI
import platform
import psutil
import time
app = FastAPI()

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "available": mem.available,
        "percent_used": mem.percent,
    }

def get_disk_usage(path='/'):
    disk = psutil.disk_usage(path)
    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent_used": disk.percent,
    }

def get_network_stats():
    net_io = psutil.net_io_counters()
    return {
        "bytes_sent": net_io.bytes_sent,
        "bytes_recv": net_io.bytes_recv,
        "packets_sent": net_io.packets_sent,
        "packets_recv": net_io.packets_recv,
    }
def get_system_info():
    system = platform.system()
    node = platform.node()
    release = platform.release()
    uname =  platform.mac_ver()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()

    return {
        "system": system,
        "node_name": node,
        "release": release,
        "version": version,
        "uname":uname,
        "machine": machine,
        "processor": processor,
    }

@app.get("/server")
async def server_info():
    system_info = get_system_info()
    return system_info

@app.get("/monitor")
async def monitoring():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    network_stats = get_network_stats()

    return {
        "timestamp": time.time(),
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage,
        "network_stats": network_stats,
    }