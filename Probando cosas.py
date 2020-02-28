import matplotlib.pyplot as plt


def clean(line: str) -> list:
    return line.replace("\n","").replace(" ","").split(",")


def times(timestamp: str) -> int:
    date_times = timestamp.split("-")
    time = [int(x) for x in date_times[1].split(":")]
    return time[0]*3600 + time[1]*60 + time[2]


f = open("/home/camila/Descargas/vacas.csv", "r")
fields = clean(f.readline())

db = {field: list() for field in fields}

row = f.readline()
while row != "":
    row = clean(row)
    for i in range(len(row)):
        db[fields[i]].append(row[i])
    row = f.readline()


db["weight"] = [int(x) for x in db["weight"]]
db["std_weight"] = [int(x) for x in db["std_weight"]]
start_time = times(db['timestamp'][0])
db["time"] = [times(x) - start_time for x in db["timestamp"]]

#Graficar
plt.plot(db["time"], db["weight"], "r.")
plt.errorbar(db["time"], db["weight"], yerr=db["std_weight"], ls="")
plt.xlabel("Time")
plt.ylabel("Weight")
plt.show()



print(fields)
print(db["time"])
f.close()


