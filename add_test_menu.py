from online_restaurant_db import Session, Menu

seafood_dishes = [
    Menu(
        name="Salmon Steak",
        weight="250g",
        ingredients="Salmon, lemon, olive oil, herbs",
        description="Grilled salmon steak with lemon and herbs.",
        price=350,
        active=True,
        file_name="salmon_steak.png"
    ),
    Menu(
        name="Seafood Risotto",
        weight="300g",
        ingredients="Rice, shrimp, mussels, squid, cream, parmesan",
        description="Creamy risotto with assorted seafood and parmesan.",
        price=320,
        active=True,
        file_name="risotto.png"
    ),
]

with Session() as session:
    session.add_all(seafood_dishes)
    session.commit()
    print("Seafood dishes added!")