import timer
import timer2


t1 = timer.Timers(5, 1, "test time")
id, duration, label, running = t1.return_info()
t1.start()
print("testing")
while t1.running:
    print(t1.get_timeout())
    t1.finished()


print("finished timer ID ", id, label, "duration: ", duration)

# t = timer2.Timers()
# t.add_timer(5,'t1', 'test')
# t.add_timer(7, 't2', "gc-r6")
# t.add_timer(4, 't3', "gc-r7")
# timers = list(t.retun_timers().keys())
# print(timers)
# print("")
# print(t.retun_timers()["t3"])
#
# t.start(timers[0])
# while timers[0] in t.retun_running_timers():
#     print("Still Running")
#     t.finished(timers[0])
