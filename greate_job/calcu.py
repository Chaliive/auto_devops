# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
import datetime
import psutil


def process():
    pids = psutil.pids()
    pro_info = []
    for pid in pids:
        try:
            eve_pro = psutil.Process(pid)
            pro_name = eve_pro.name()  # 进程名
            pro_status = eve_pro.status()  # 进程状态
            pro_mmr_per = eve_pro.memory_percent()  # 进程内存利用率
            pro_num_thr = eve_pro.num_threads()  # 进程开启的线程数
            pro_time = eve_pro.create_time()  # 进程开启的时间
            dateArray = datetime.datetime.fromtimestamp(pro_time)  # 时间可视化
            # dateArray = datetime.datetime.utcfromtimestamp(pro_time)  # 标准时间
            v_time = dateArray.strftime("%Y-%m-%d %H:%M:%S")
            pro = [pro_name, pid, pro_status, '%.2f' % pro_mmr_per, pro_num_thr, v_time]
            pro_info.append(pro)
        except:
            process()
    return pro_info


def cpu():
    cpu_per = psutil.cpu_percent(1)
    sys_time = datetime.datetime.now().strftime("%H:%M:%S")  # 系统时间
    cpu_time = [cpu_per, sys_time]
    # print('cpu使用情况是: %s' % cpu_time)
    return cpu_time


def memory():
    free = (round(psutil.virtual_memory().free / (1024 * 1024 * 1024), 2))
    total = (round(psutil.virtual_memory().total / (1024 * 1024 * 1024)))
    used = total - free
    memory = used / total
    mmr_info = [free, total, used, memory]
    # print(memory)
    return mmr_info


def disk():
    disk_info = {}
    diskinfo = psutil.disk_partitions()  # 获取所有磁盘信息
    for disk in [diskinfo[0].device, diskinfo[1].device, diskinfo[2].device]:
        totaldisk = psutil.disk_usage(disk).total / 1024 / 1024 / 1024
        useddisk = psutil.disk_usage(disk).used / 1024 / 1024 / 1024
        freedisk = psutil.disk_usage(disk).free / 1024 / 1024 / 1024
        disk_info[disk] = ['%.2f' % (totaldisk), '%.2f' % (useddisk), '%.2f' % (freedisk)]
    # part = psutil.disk_io_counters(perdisk=True)
    read_count = psutil.disk_io_counters().read_count / 1024
    write_count = psutil.disk_io_counters().write_count / 1024
    disk_info['io'] = [read_count, write_count]
    return disk_info


def net():
    # e_net = psutil.net_io_counters(pernic=True)  # pernic=True输出每个网络接口的IO信息
    bytes_sent = psutil.net_io_counters().bytes_sent / 1024
    bytes_recv = psutil.net_io_counters().bytes_recv / 1024
    e_net = ['%.2f' % bytes_sent, '%.2f' % bytes_recv]
    return e_net

