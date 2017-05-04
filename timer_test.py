import timer


t1 = timer.Timers(5, 1, "test time")
print(t1.running)
t1.start()
print("testing")
while t1.running:
    print(t1.get_timeout())
    t1.finished()

print(t1.running)
print("Done")
