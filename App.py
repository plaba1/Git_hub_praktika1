Session = sessionmaker(bind=engine)
session = Session()

while True:
    pirmas_meniu = input('1. ivesti username ir slaptazodi\n2.kurti nauja vartotoja\n3. ieskoti skelbimu\nq. iseiti is programos\n')
    print('-' * 50)
    if pirmas_meniu == '1':
        username = input('iveskite username:\n')
        slaptazodis = input('iveskite slaptazodi:\n')
        print('-' * 50)
        eil_obj = session.query(Vartotojas).filter_by(username=username).all()