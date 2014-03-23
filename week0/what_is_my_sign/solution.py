SIGNS = [ "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini",
            "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Saggitarius" ]
RANGES = [ range(1,20), range(1,19), range(1,21), range(1, 21),
            range(1,21), range(1,21), range(1,22), range(1,23), range(1,23),
            range(1,23), range(1,22), range(1,22), range(20,32), range(19,30),
            range(21,32), range(21, 31), range(21,32), range(21,31),
            range(22,32), range(23,32), range(23,31), range(23,32),
            range(22,31), range(22,32) ]


def what_is_my_sign(day, month):
    for i in range(0, len(RANGES) + 1):
        if day in RANGES[i] and (i == month or i == month + 11):
            if i < 12:
                return SIGNS[i - 1]
            else:
                return SIGNS[i - 11]
