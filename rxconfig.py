import reflex as rx

config = rx.Config(
    app_name="pet_projects",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)