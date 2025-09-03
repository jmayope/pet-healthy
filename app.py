import flet as ft
from typing import List
from models.customer import Customer
from models.animal import Animal

def main(page: ft.Page):
    page.title = "Mascota Saludable"

    customers: List[Customer] = []

    content_new_customer = ft.Row()
    content_pets = ft.Column()
    content_customers = ft.Column()

    customer_name = ft.TextField(value="", width=100)

    def add_pet(e):
        name = ft.TextField(value="", label="Nombre", width=100)
        age = ft.TextField(value="", label="Edad", width=100)
        content_pets.controls.append(
            ft.Row(
                [
                    name,
                    age
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        page.update()

    def render_customers():
        content_customers.controls = []
        content_new_customer.controls = []
        for i in customers:
            content_pets_of_customer = ft.Column()
            for p in i.pets:
                content_pets_of_customer.controls.append(
                    ft.Row(
                        [
                            ft.Text(
                                value=f"{p.name}"
                            ),
                            ft.Dropdown(
                                
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )

                )

            content_customers.controls.append(
                ft.Row(
                    [
                        ft.Text(
                            value=i.name
                        ),
                        ft.Text(
                            value=f"{len(i.pets)} mascotas"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Column(
                    [

                    ]
                )
            )
        
        page.update()

    def save_customer(e):
        pets_of_customer = []
        for row in content_pets.controls:
            name_field = row.controls[0].value
            age_field = row.controls[1].value   
            pets_of_customer.append(Animal(name_field, age_field))
        
        
        customers.append(Customer(customer_name.value, pets_of_customer))
        content_new_customer.controls = []
        content_pets.controls = []
        render_customers()

    def add_customer(e):
        customer_name.value = ""
        
        page.update()
        content_new_customer.controls.append(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(
                                value="Nombre"
                            ),
                            customer_name
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Row(
                        [
                            ft.Text(
                                value="Mascotas"
                            ),
                            ft.ElevatedButton(
                                text="Agregar",
                                on_click=add_pet
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    content_pets,
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                text="Guardar",
                                on_click=save_customer
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            )
        )
        page.update()

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            value="Mascota Saludable"
                        ),
                        ft.ElevatedButton(
                            text="Agregar Cliente",
                            on_click=add_customer
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(),
                content_new_customer,
                ft.Divider(),
                content_customers

            ]
        )
    )

ft.app(main)