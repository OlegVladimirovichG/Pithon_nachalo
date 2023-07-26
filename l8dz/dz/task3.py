from task3_mod import work_with_files as wwf, another_var as anw
import time

tries = []
for _  in range(10):
    start_time = time.time()
    wwf.generate_dict('D:\\Курсы', './out')
    tries.append(time.time() - start_time)
print("Мой вариант: %s секунд" % (mean(tries)))

tries = []
for _  in range(10):
    start_time = time.time()
    anw.folders_info('D:\\Курсы', './out')
    tries.append(time.time() - start_time)
print("Вариант Анатолия: %s секунд" % (mean(tries)))