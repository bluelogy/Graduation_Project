from icmplib import ping
from fastapi import FastAPI
def run_ping(target):
    result = ping(target, count=4, interval=0.5, timeout= 2)
    return {
        "host": target,
        "alive": result.is_alive,
        "avg_ms": result.avg_rtt,
        "jitter_ms": result.jitter,
        "loss_percent": result.packet_loss * 100,
    }

targets= ["itcraft.ddns.net", "dumbo.site", "1.1.1.1"]

for t in targets:
    try:
        r = run_ping(t)
        print(f"Host: {r['host']:<15}, Alive: {str(r['alive']):<15}, Average Latency: {r['avg_ms']:<4.1f}, Packet loss: {r['loss_percent']:<15}")
    except Exception as e:
        print(f"{t} FAILED: {e}")

