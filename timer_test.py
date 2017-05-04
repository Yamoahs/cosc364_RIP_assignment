import timer


t1 = timer.Timers(5, 1, "test time")
t1.start()
print("testing")

print(t1.get_timeout())
timer.time.sleep(10)
print(t1.finished())
