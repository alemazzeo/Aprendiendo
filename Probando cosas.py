import numpy as np
import matplotlib.pyplot as plt


def open_csv(path: str) -> dict:

    def _clean(line: str) -> list:
        return line.replace("\n", "").replace(" ", "").split(",")

    def _times(timestamp: str) -> int:
        date_times = timestamp.split("-")
        time = [int(x) for x in date_times[1].split(":")]
        return time[0]*3600 + time[1]*60 + time[2]

    f = open(path, "r")
    fields = _clean(f.readline())

    _db = {field: list() for field in fields}

    row = f.readline()
    while row != "":
        row = _clean(row)
        for i in range(len(row)):
            _db[fields[i]].append(row[i])
        row = f.readline()

    _db["weight"] = np.array([int(x) for x in _db["weight"]])
    _db["std_weight"] = np.array([int(x) for x in _db["std_weight"]])
    start_time = _times(_db['timestamp'][0])
    _db["time"] = np.array([_times(x) - start_time for x in _db["timestamp"]])
    f.close()
    return _db


db = open_csv(path="/home/camila/Descargas/vacas.csv")
diff = db["time"][1:]-db["time"][0:-1]


# Plot
plt.plot(db["time"], db["weight"], "r.")
plt.errorbar(db["time"], db["weight"], yerr=db["std_weight"], ls="")
plt.xlabel("Time")
plt.ylabel("Weight")
plt.show()

plt.plot(diff)
plt.show()

print(len(db["time"]))
print(diff)
print(db["time"])



