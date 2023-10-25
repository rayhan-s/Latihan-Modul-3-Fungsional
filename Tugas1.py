def konversi(j=0):
    def minggu(mg=0):
        def hari(hr=0):
            def jam(jm=0):
                def menit(mn=0):
                    return (((j * 7 + mg) * 24 + hr) * 60 + jm) * 60 + mn
                return menit
            return jam
        return hari
    return minggu


data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

results = []
for entry in data:
    parts = entry.split()
    minggu = int(parts[0])
    hari = int(parts[2])
    jam = int(parts[4])
    menit = int(parts[6])

    konvert = konversi()(minggu)(hari)(jam)(menit)
    results.append(konvert)

print("hasil konversi", results)
