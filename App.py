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
        for eil_o in eil_obj:
            if eil_o.slaptazodis == slaptazodis:
                eil_objs = session.query(Vartotojas).filter_by(username=username).one()
                print('iejome i pagrindini meniu')
                antras_meniu = input('1.ivesti nauja objekta\n2. ivesti nauja skelbima\n q. iseiti\n')
                if antras_meniu == '1':
                    objektas_o = Objektas(adresas=input('iveskite adresa:\n'),
                                          objekto_tipas=input('iveskite objekto tipa: butas/namas\n'),
                                          plotas=input('iveskite plota:\n'),
                                          miestas=input('iveskite miesta\n',
                                                        vartotojas_id=eil_objs.id)
                                          )
                    session.add(objektas_o)
                    session.commit()
                    print('objektas pridetas')
                    print('-' * 50)

                elif antras_meniu == '2':
                    skelbimas_o = Skelbimas(kaina=input('iveskite kaina:\n'),
                                            nuoma_pardavimas=input('iveskite ar objektas pardavimui ar nuomai:\n'),
                                            tekstas=input('iveskite skelbimo teksta:\n'),
                                            agentura_id=input('iveskite agenturos id\n'),
                                            objektas_id=input('iveskite objekto id\n')
                                            )
                    agentura_o.skelbimas1.append(skelbimas_o)
                    session.add(skelbimas_o)
                    session.commit()
                    print('skelbimas pridetas')
                    print('-' * 50)

            else:
                print('neteisingas username arba slaptazodis')
    elif pirmas_meniu == '2':
        username = input('iveskite username:\n')
        slaptazodis = input('iveskite slaptazodi:\n')
        vartotojas_o = Vartotojas(vardas=input('iveskite savo varda:\n'),
                                  pavarde=input('iveskite savo pavarde:\n'),
                                  tel_nr=input('iveskite telefono numeri:\n'),
                                  username=username,
                                  slaptazodis=slaptazodis
                                  )
        session.add(vartotojas_o)
        session.commit()
    elif pirmas_meniu == '3':
        antras_meniu = input('1. rodyti visus skelbimus\n2. filtruoti skelbimus\nq- iseiti\n')
        if antras_meniu == '1':
            skelbimas_o1 = session.query(Skelbimas).all()
            agentura_o1 = session.query(Agentura).all()
            vartotojas_o1 = session.query(Vartotojas).all()
            objektas_o1 = session.query(Objektas).all()
            for skelb in skelbimas_o1:
                # print(skelb.kaina, skelb.nuoma_pardavimas, skelb.tekstas, skelb.agentura_id, skelb.objektas_id,
                #       agentura_o1[skelb.agentura_id-1].pavadinimas,
                #
                #       objektas_o1[skelb.objektas_id - 1].objekto_tipas,
                #       objektas_o1[skelb.objektas_id - 1].plotas,
                #       objektas_o1[skelb.objektas_id - 1].vzz\artotojas_id,
                #       objektas_o1[skelb.objektas_id - 1].miestas,
                #       vartotojas_o1[objektas_o1[skelb.objektas_id-1].vartotojas_id-1].vardas
                #       )
                print(
                    f'agentura: {agentura_o1[skelb.agentura_id - 1].pavadinimas}, {objektas_o1[skelb.objektas_id - 1].objekto_tipas},'
                    f' plotas {objektas_o1[skelb.objektas_id - 1].plotas} m2, miestas: {objektas_o1[skelb.objektas_id - 1].miestas},'
                    f' adresas: {objektas_o1[skelb.objektas_id - 1].adresas}, kaina: {skelb.kaina} eur, savininkas '
                    f'{objektas_o1[skelb.objektas_id - 1].vartotojas1.vardas} {objektas_o1[skelb.objektas_id - 1].vartotojas1.pavarde}')
                print('-' * 50)
        if antras_meniu == '2':
            trecias_meniu = input('1. filtruoti pagal miesta\n2. filtruoti pagal kaina\n')
            if trecias_meniu == '1':
                miestas = input('iveskite miesto pavadinima:\n')
                skelbimas_o1 = session.query(Skelbimas).all()
                agentura_o1 = session.query(Agentura).all()
                vartotojas_o1 = session.query(Vartotojas).all()
                objektas_o1 = session.query(Objektas).filter(Objektas.miestas.ilike(f'%{miestas}%')).all()

                for miest in objektas_o1:
                    skelbimas_o2 = session.query(Skelbimas).filter_by(objektas_id=miest.id).all()
                    for objs in skelbimas_o2:
                        print(
                            f'{objs.kaina}, {objs.nuoma_pardavimas}, {objs.tekstas}, {miest.miestas}, {miest.adresas}, {miest.objekto_tipas}, {miest.plotas}')
                        print('-' * 50)

            if trecias_meniu == '2':
                kaina_nuo = float(input('iveskite kaina nuo:\n'))
                kaina_iki = float(input('iveskite kaina iki:\n'))
                skelbimas_o3 = session.query(Skelbimas).filter(Skelbimas.kaina > kaina_nuo,
                                                               Skelbimas.kaina < kaina_iki).all()
                agentura_o1 = session.query(Agentura).all()
                vartotojas_o1 = session.query(Vartotojas).all()
                objektas_o1 = session.query(Objektas).all()

                for kain in skelbimas_o3:
                    objs = session.query(Objektas).filter_by(id=kain.objektas_id).all()
                    print(
                        f'{kain.nuoma_pardavimas}, {kain.kaina}, {objektas_o1[kain.objektas_id - 1].adresas}, {objektas_o1[kain.objektas_id - 1].miestas}')
                    print('-' * 50)

                # for obj in objektas_o1:
                #     print(obj.miestas, obj.vartotojas_id)
                #     print(
                #         f'agentura: {agentura_o1[skelb.agentura_id - 1].pavadinimas}, {objektas_o1[skelb.objektas_id - 1].objekto_tipas},'
                #         f' plotas {obj.plotas} m2, miestas: {obj.miestas},'
                #         f' adresas: {obj.adresas}')
                #     print('-' * 30)



    elif pirmas_meniu == 'q':
        break
    else:
        print('neteisinga ivestis')
