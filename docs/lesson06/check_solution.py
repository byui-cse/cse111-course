def modify_arguments(b, i, f, t, s, d):
	b = True
	i = 2
	f = 4.5
	t[0] = 30
	t.append(21)
	s.add("bass")
	s.remove("flute")
	d["Carlos"] = 10
	d["Mijken"] = 14


def main():
	bo = False
	it = 1
	fl = 15.2
	ls = [24, 25, 26]
	st = {"drum", "guitar", "ukulele", "flute"}
	di = {"Lena":6, "Carlos":7}
	print(bo, it, fl, ls, st, di, sep="; ")
	modify_arguments(bo, it, fl, ls, st, di)
	print(bo, it, fl, ls, st, di, sep="; ")

main()
