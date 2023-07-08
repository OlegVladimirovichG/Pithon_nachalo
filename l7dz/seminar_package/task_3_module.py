def work_with_files(num_file, name_file, result_file):
    with (
        open(num_file, "r", encoding="utf-8") as num_f,
        open(name_file, "r", encoding="utf-8") as name_f,
        open(result_file, "w", encoding="utf-8") as res_f
    ):
        num = [s.strip() for s in num_f]
        name = [s.strip() for s in name_f]
        if len(num) > len(name):
            name = name + name[:len(num) - len(name)]
        elif len(num) < len(name):
            num = num + num[:len(name) - len(num)]
        for i in range(len(num)):
            num_1, num_2 = num[i].split("|")
            prod = int(num_1) * float(num_2)
            if prod < 0:
                res_f.write(f"{name[i].lower()} - {-prod}\n")
            elif prod > 0:
                res_f.write(f"{name[i].upper()} - {round(prod)}\n")