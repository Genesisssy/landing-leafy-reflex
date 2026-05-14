import reflex as rx

config = rx.Config(
    app_name="leafy_landing_reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)