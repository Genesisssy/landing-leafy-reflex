import reflex as rx

PRIMARY = "#8B6B4A"
BACKGROUND = "#F7F1EB"
TEXT = "#3E2C23"
MUTED = "#8E7B70"
ACCENT = "#D4A574"
LIGHT_BG = "#F3EAE2"


class State(rx.State):
    pass


# ─────────────────────────────────────────────
#  SVG ICONS  (igual a la foto original)
# ─────────────────────────────────────────────

def icon_shipping():
    """Reloj / Envío rápido"""
    return rx.html(
        '<svg width="52" height="52" viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<circle cx="26" cy="26" r="22" stroke="#8B6B4A" stroke-width="2"/>'
        '<path d="M26 16v10l7 5" stroke="#8B6B4A" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '</svg>'
    )


def icon_design():
    """Joya / Diseño exclusivo"""
    return rx.html(
        '<svg width="52" height="52" viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<path d="M26 8l5 10H41l-8 7 3 11-10-6-10 6 3-11-8-7h10z" stroke="#8B6B4A" stroke-width="2" stroke-linejoin="round"/>'
        '</svg>'
    )


def icon_packaging():
    """Caja / Empaque"""
    return rx.html(
        '<svg width="52" height="52" viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<rect x="9" y="22" width="34" height="22" rx="3" stroke="#8B6B4A" stroke-width="2"/>'
        '<path d="M17 22v-5a9 9 0 0118 0v5" stroke="#8B6B4A" stroke-width="2"/>'
        '<path d="M9 29h34" stroke="#8B6B4A" stroke-width="2"/>'
        '<path d="M26 29v15" stroke="#8B6B4A" stroke-width="2"/>'
        '</svg>'
    )


def icon_quality():
    """Escudo / Calidad"""
    return rx.html(
        '<svg width="52" height="52" viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<path d="M26 8l17 7v12c0 9-8 15-17 18C17 42 9 36 9 27V15z" stroke="#8B6B4A" stroke-width="2" stroke-linejoin="round"/>'
        '<path d="M19 26l4.5 4.5 9-9" stroke="#8B6B4A" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '</svg>'
    )


def icon_bag():
    """Bolsa de compras para las tarjetas de producto"""
    return rx.html(
        '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<path d="M5 7V5a4 4 0 018 0v2" stroke="#8B6B4A" stroke-width="1.6" stroke-linecap="round"/>'
        '<rect x="2" y="7" width="14" height="9" rx="2" stroke="#8B6B4A" stroke-width="1.6"/>'
        '</svg>'
    )


def icon_shimmer_logo():
    """Logo estrella de Shimmer"""
    return rx.html(
        '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<path d="M9 1l1.8 5.5H17l-4.8 3.4 1.8 5.5L9 12l-5 3.4 1.8-5.5L1 6.5h6.2z" fill="white"/>'
        '</svg>'
    )


# ─────────────────────────────────────────────
#  NAVBAR
# ─────────────────────────────────────────────

def navbar():
    return rx.box(
        # Logo Shimmer - izquierda
        rx.hstack(
            rx.box(
                icon_shimmer_logo(),
                width="36px",
                height="36px",
                border_radius="50%",
                bg=TEXT,
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.heading("Shimmer", size="5", color=TEXT, font_weight="bold"),
            spacing="2",
            position="absolute",
            left="70px",
            top="32px",
            z_index="50",
        ),
        # Barra blanca centrada
        rx.hstack(
            rx.link("Home", href="/", color=TEXT, text_decoration="none",
                    font_size="0.85rem", font_weight="500", _hover={"color": PRIMARY}),
            rx.link("About Us", href="/learn-more", color=TEXT, text_decoration="none",
                    font_size="0.85rem", font_weight="500", _hover={"color": PRIMARY}),
            rx.link("Collections", href="/", color=TEXT, text_decoration="none",
                    font_size="0.85rem", font_weight="500", _hover={"color": PRIMARY}),
            rx.hstack(
                rx.text("Pages", color=TEXT, font_size="0.85rem", font_weight="500"),
                rx.text("▾", color=TEXT, font_size="0.65rem"),
                spacing="1",
                cursor="pointer",
            ),
            rx.link(
                rx.button(
                    "Contact Us",
                    bg=TEXT,
                    color="white",
                    border_radius="999px",
                    font_size="0.78rem",
                    padding_x="1.5rem",
                    padding_y="0.6rem",
                    _hover={"bg": PRIMARY},
                    transition="all 0.3s ease",
                    cursor="pointer",
                ),
                href="/learn-more",
                text_decoration="none",
            ),
            align="center",
            spacing="8",
            bg="rgba(255,255,255,0.97)",
            padding="0.9rem 2rem",
            border_radius="999px",
            position="absolute",
            top="32px",
            left="50%",
            transform="translateX(-50%)",
            z_index="50",
            box_shadow="0 4px 15px rgba(0,0,0,0.1)",
        ),
        position="relative",
        width="100%",
        height="130px",
    )


# ─────────────────────────────────────────────
#  TARJETAS FLOTANTES
# ─────────────────────────────────────────────

def stats_card():
    """230K Happy Clients con avatares apilados"""
    return rx.box(
        rx.hstack(
            # Avatares circulares apilados
            rx.box(
                rx.box(width="28px", height="28px", border_radius="50%",
                       bg="#C4916A", border="2px solid white"),
                rx.box(width="28px", height="28px", border_radius="50%",
                       bg="#A87850", border="2px solid white", margin_left="-10px"),
                rx.box(width="28px", height="28px", border_radius="50%",
                       bg="#D4A574", border="2px solid white", margin_left="-10px"),
                rx.box(
                    rx.text("+", color="white", font_size="0.7rem", font_weight="bold"),
                    width="28px", height="28px", border_radius="50%",
                    bg=TEXT, border="2px solid white",
                    display="flex", align_items="center", justify_content="center",
                    margin_left="-10px",
                ),
                display="flex",
                flex_direction="row",
                align_items="center",
            ),
            rx.vstack(
                rx.text("230K", font_weight="bold", font_size="1.5rem", color=TEXT, line_height="1"),
                rx.text("Happy Clients", color=MUTED, font_size="0.7rem", font_weight="600"),
                align="start",
                spacing="0",
            ),
            spacing="3",
            align="center",
        ),
        bg="rgba(255,255,255,0.97)",
        padding="1rem 1.4rem",
        border_radius="22px",
        position="absolute",
        right="110px",
        top="185px",
        box_shadow="0 12px 35px rgba(0,0,0,0.13)",
        z_index="40",
        _hover={"box_shadow": "0 18px 45px rgba(0,0,0,0.18)", "transform": "translateY(-4px)"},
        transition="all 0.3s ease",
        cursor="pointer",
    )


def product_floating():
    """Tarjeta Beautiful In Every Detail"""
    return rx.box(
        rx.hstack(
            rx.image(
                src="/necklace.png",
                width="78px",
                height="60px",
                object_fit="cover",
                border_radius="12px",
            ),
            rx.vstack(
                rx.text("Beautiful In Every Detail",
                        font_weight="bold", font_size="0.78rem",
                        color=TEXT, line_height="1.3"),
                rx.hstack(
                    rx.text("Read More", color=PRIMARY,
                            font_size="0.68rem", font_weight="700"),
                    rx.box(
                        rx.text("→", color=PRIMARY, font_size="0.65rem"),
                        bg=LIGHT_BG, border_radius="50%",
                        width="18px", height="18px",
                        display="flex", align_items="center", justify_content="center",
                    ),
                    spacing="2", align="center",
                ),
                align="start",
                spacing="1",
            ),
            spacing="3",
            align="center",
        ),
        bg="rgba(255,255,255,0.97)",
        padding="1.2rem 1.4rem",
        border_radius="22px",
        position="absolute",
        right="130px",
        bottom="60px",
        box_shadow="0 12px 35px rgba(0,0,0,0.13)",
        z_index="40",
        _hover={"box_shadow": "0 18px 45px rgba(0,0,0,0.18)", "transform": "translateY(-4px)"},
        transition="all 0.3s ease",
        cursor="pointer",
    )


# ─────────────────────────────────────────────
#  HERO SECTION
# ─────────────────────────────────────────────

def hero_section():
    return rx.box(
        navbar(),
        stats_card(),
        product_floating(),
        rx.vstack(
            rx.heading(
                "Our Luxury\nCollections",
                white_space="pre-line",
                font_size="5.5rem",
                line_height="0.9",
                color="white",
                font_weight="400",
                letter_spacing="-0.02em",
            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        "Let's Get Started",
                        bg="white",
                        color=TEXT,
                        border_radius="999px",
                        padding_x="1.8rem",
                        padding_y="0.75rem",
                        font_size="0.82rem",
                        font_weight="700",
                        _hover={"bg": ACCENT, "color": "white"},
                        transition="all 0.3s ease",
                        cursor="pointer",
                    ),
                    href="/learn-more",
                    text_decoration="none",
                ),
                rx.button(
                    "→",
                    bg="rgba(255,255,255,0.2)",
                    color="white",
                    border_radius="50%",
                    width="44px",
                    height="44px",
                    font_size="1.2rem",
                    border="none",
                    _hover={"bg": "rgba(255,255,255,0.35)", "transform": "translateX(5px)"},
                    transition="all 0.3s ease",
                    cursor="pointer",
                    on_click=rx.redirect("/learn-more"),
                ),
                spacing="2",
                margin_top="1.5rem",
            ),
            rx.vstack(
                rx.text("// Shimmer Jewelry Store",
                        color="rgba(255,255,255,0.92)",
                        font_size="0.72rem", font_weight="700",
                        letter_spacing="0.1em"),
                rx.text(
                    "Lorem ipsum dolor sit amet, consectetur\nadipiscing elit. Ut sit tellus, luctus nec\nullamcorper mattis, pulvinar dapibus leo.",
                    white_space="pre-line",
                    color="rgba(255,255,255,0.8)",
                    font_size="0.82rem",
                    max_width="340px",
                    line_height="1.8",
                ),
                spacing="1",
                margin_top="2rem",
            ),
            align="start",
            spacing="3",
            padding_left="110px",
            padding_top="150px",
            padding_bottom="100px",
        ),
        background_image="url('/hero.png')",
        background_size="cover",
        background_position="center right",
        background_repeat="no-repeat",
        border_radius="32px",
        width="100%",
        position="relative",
        overflow="hidden",
        min_height="580px",
    )


# ─────────────────────────────────────────────
#  BENEFITS
# ─────────────────────────────────────────────

def benefit_item(icon_comp, title, description):
    return rx.vstack(
        rx.box(
            icon_comp,
            _hover={"transform": "scale(1.12)"},
            transition="all 0.3s ease",
            cursor="pointer",
            margin_bottom="0.5rem",
        ),
        rx.heading(title, size="4", color=TEXT, text_align="center", font_weight="600"),
        rx.text(
            description,
            white_space="pre-line",
            font_size="0.82rem",
            color=MUTED,
            text_align="center",
            line_height="1.6",
        ),
        spacing="2",
        align="center",
        padding="2rem 1.5rem",
        border_radius="18px",
        _hover={"bg": "rgba(212,165,116,0.1)", "transform": "translateY(-4px)"},
        transition="all 0.3s ease",
        cursor="pointer",
    )


def benefits_section():
    return rx.grid(
        benefit_item(icon_shipping(), "Free Shipping",
                     "Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit."),
        benefit_item(icon_design(), "Exclusive Design",
                     "Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit."),
        benefit_item(icon_packaging(), "Good Packaging",
                     "Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit."),
        benefit_item(icon_quality(), "Highest Quality",
                     "Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit."),
        columns="4",
        spacing="6",
        width="100%",
        padding="4rem 3rem",
        bg=LIGHT_BG,
        border_radius="28px",
    )


# ─────────────────────────────────────────────
#  FEATURED
# ─────────────────────────────────────────────

def featured_section():
    return rx.flex(
        # Imagen izquierda con badge de estrellas
        rx.box(
            rx.image(
                src="/model.png",
                width="420px",
                height="380px",
                object_fit="cover",
                border_radius="24px",
            ),
            rx.box(
                rx.hstack(
                    rx.text("★★★★★", color="#F59E0B", font_size="0.7rem"),
                    rx.text("(5/5)", color="white", font_size="0.68rem"),
                    spacing="1",
                ),
                position="absolute",
                top="14px",
                left="14px",
                bg="rgba(0,0,0,0.45)",
                padding="5px 12px",
                border_radius="999px",
            ),
            position="relative",
            _hover={"transform": "scale(1.02)"},
            transition="all 0.4s ease",
            cursor="pointer",
        ),
        # Contenido central
        rx.vstack(
            rx.heading(
                "The Art Of Radiant\nRefinement",
                white_space="pre-line",
                font_size="3rem",
                line_height="1.1",
                color=TEXT,
                font_weight="500",
            ),
            rx.text(
                "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor "
                "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
                "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure "
                "dolor in reprehenderit in voluptate velit esse cillum dolore eu.",
                color=MUTED,
                font_size="0.9rem",
                line_height="1.8",
                max_width="360px",
            ),
            rx.link(
                rx.button(
                    "Learn More",
                    bg="white",
                    color=TEXT,
                    border_radius="999px",
                    padding_x="2.2rem",
                    padding_y="0.85rem",
                    font_size="0.85rem",
                    font_weight="600",
                    border=f"1.5px solid {MUTED}",
                    _hover={"bg": PRIMARY, "color": "white", "border_color": PRIMARY},
                    transition="all 0.3s ease",
                    cursor="pointer",
                ),
                href="/learn-more",
                text_decoration="none",
            ),
            align="start",
            spacing="5",
            flex="1",
            padding_x="2rem",
        ),
        # Imagen derecha
        rx.box(
            rx.image(
                src="/ring.png",
                width="210px",
                height="290px",
                object_fit="cover",
                border_radius="24px",
            ),
            _hover={"transform": "scale(1.02)"},
            transition="all 0.4s ease",
            cursor="pointer",
        ),
        justify="between",
        align="center",
        spacing="6",
        width="100%",
        padding_y="1rem",
    )


# ─────────────────────────────────────────────
#  PRODUCTS
# ─────────────────────────────────────────────

def product_card(image, title, price):
    return rx.vstack(
        rx.box(
            rx.image(
                src=image,
                width="100%",
                height="200px",
                object_fit="cover",
                border_radius="20px",
            ),
            # Icono de bolsa en la esquina
            rx.box(
                icon_bag(),
                position="absolute",
                top="12px",
                right="12px",
                bg="white",
                border_radius="50%",
                width="36px",
                height="36px",
                display="flex",
                align_items="center",
                justify_content="center",
                box_shadow="0 2px 8px rgba(0,0,0,0.12)",
                _hover={"bg": LIGHT_BG, "transform": "scale(1.1)"},
                transition="all 0.3s ease",
                cursor="pointer",
            ),
            position="relative",
            _hover={"transform": "scale(1.04)"},
            transition="all 0.3s ease",
            cursor="pointer",
        ),
        rx.heading(title, size="4", color=TEXT, font_weight="600"),
        rx.text(f"${price}", font_size="0.92rem", color=MUTED, font_weight="600"),
        spacing="2",
        width="100%",
        align="start",
    )


def products_section():
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.heading("Our Collection", size="7", color=TEXT, font_weight="500"),
                rx.text(
                    "Lorem ipsum dolor sit amet consectetur adipiscing elit. "
                    "Ut sit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.",
                    color=MUTED, font_size="0.9rem",
                    max_width="260px", line_height="1.7",
                ),
                rx.link(
                    rx.button(
                        "See More",
                        bg="white",
                        color=TEXT,
                        border_radius="999px",
                        padding_x="1.8rem",
                        padding_y="0.7rem",
                        font_size="0.82rem",
                        font_weight="600",
                        border=f"1.5px solid {MUTED}",
                        _hover={"bg": PRIMARY, "color": "white"},
                        transition="all 0.3s ease",
                        cursor="pointer",
                    ),
                    href="/learn-more",
                    text_decoration="none",
                ),
                align="start",
                spacing="4",
                width="280px",
                flex_shrink="0",
            ),
            rx.grid(
                product_card("/goldearing.png", "Gold Earring", "240.00"),
                product_card("/diamondring.png", "Diamond Ring", "240.00"),
                product_card("/necklace.png", "Gold Necklace", "240.00"),
                columns="3",
                spacing="5",
                flex="1",
            ),
            spacing="8",
            width="100%",
            align="center",
        ),
        bg="white",
        border_radius="28px",
        padding="4rem",
    )


# ─────────────────────────────────────────────
#  CATEGORIES
# ─────────────────────────────────────────────

def category_item(image, title):
    return rx.vstack(
        rx.box(
            rx.image(
                src=image,
                width="110px",
                height="110px",
                object_fit="cover",
                border_radius="999px",
            ),
            border=f"6px solid #F5EEE7",
            border_radius="999px",
            width="110px",
            height="110px",
            overflow="hidden",
            _hover={"transform": "scale(1.1)", "box_shadow": "0 10px 25px rgba(0,0,0,0.15)"},
            transition="all 0.3s ease",
            cursor="pointer",
        ),
        rx.text(title, color=TEXT, font_weight="600", font_size="0.95rem"),
        rx.box(
            rx.text("+", color="white", font_size="0.8rem", font_weight="bold"),
            bg=TEXT,
            border_radius="50%",
            width="24px",
            height="24px",
            display="flex",
            align_items="center",
            justify_content="center",
            _hover={"bg": PRIMARY, "transform": "scale(1.1)"},
            transition="all 0.3s ease",
            cursor="pointer",
        ),
        spacing="2",
        align="center",
    )


def categories_section():
    return rx.flex(
        # Imagen izquierda con botón play
        rx.box(
            rx.image(
                src="/collection.png",
                width="480px",
                height="340px",
                object_fit="cover",
                border_radius="24px",
            ),
            rx.box(
                rx.box(
                    rx.text("▶", color=TEXT, font_size="1rem"),
                    bg="rgba(255,255,255,0.92)",
                    border_radius="50%",
                    width="54px",
                    height="54px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    box_shadow="0 4px 20px rgba(0,0,0,0.2)",
                    _hover={"transform": "scale(1.1)", "bg": "white"},
                    transition="all 0.3s ease",
                    cursor="pointer",
                ),
                position="absolute",
                top="50%",
                left="50%",
                transform="translate(-50%, -50%)",
            ),
            position="relative",
            _hover={"transform": "scale(1.02)"},
            transition="all 0.4s ease",
            cursor="pointer",
        ),
        # Contenido derecho
        rx.vstack(
            rx.heading("Choose The Type!", size="7", color=TEXT, font_weight="500"),
            rx.text(
                "Lorem ipsum dolor sit amet consectetur adipiscing elit. "
                "Ut elit tellus, luctus nec ullamcorper mattis.",
                color=MUTED, font_size="0.92rem",
                max_width="400px", line_height="1.7",
            ),
            rx.hstack(
                category_item("/ringcategory.png", "Ring"),
                category_item("/necklacecategory.png", "Necklace"),
                category_item("/braceletcategory.png", "Bracelet"),
                spacing="8",
            ),
            align="start",
            spacing="5",
            flex="1",
            padding_left="2rem",
        ),
        justify="between",
        align="center",
        spacing="8",
        width="100%",
    )


# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────

def footer_logo(svg_code, name, superscript="®"):
    return rx.hstack(
        rx.html(svg_code),
        rx.hstack(
            rx.text(name, font_weight="700", font_size="0.9rem", color=TEXT),
            rx.text(superscript, color=TEXT, font_size="0.6rem", align_self="start", margin_top="2px"),
            spacing="0",
        ),
        spacing="2",
        align="center",
        cursor="pointer",
        _hover={"opacity": "0.65"},
        transition="all 0.3s ease",
    )


def footer():
    return rx.hstack(
        footer_logo(
            '<svg width="22" height="22" viewBox="0 0 22 22" fill="none">'
            '<path d="M4 11c0-3.9 3.1-7 7-7s7 3.1 7 7-3.1 7-7 7" stroke="#3E2C23" stroke-width="1.8" stroke-linecap="round"/>'
            '<circle cx="11" cy="11" r="2.5" fill="#3E2C23"/>'
            '<path d="M11 4v2M11 16v2M4 11H6M16 11h2" stroke="#3E2C23" stroke-width="1.5" stroke-linecap="round"/>'
            '</svg>',
            "logoipsum",
        ),
        footer_logo(
            '<svg width="22" height="22" viewBox="0 0 22 22" fill="none">'
            '<circle cx="11" cy="11" r="9" stroke="#3E2C23" stroke-width="1.8"/>'
            '<path d="M7 11l3 3 5-5" stroke="#3E2C23" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
            '</svg>',
            "logoipsum",
            "",
        ),
        footer_logo(
            '<svg width="22" height="22" viewBox="0 0 22 22" fill="none">'
            '<rect x="3" y="3" width="16" height="16" rx="3" stroke="#3E2C23" stroke-width="1.8"/>'
            '<path d="M11 7v10M7 11h8" stroke="#3E2C23" stroke-width="1.8" stroke-linecap="round"/>'
            '</svg>',
            "logoipsum",
        ),
        footer_logo(
            '<svg width="22" height="22" viewBox="0 0 22 22" fill="none">'
            '<path d="M3 7h16M3 11h16M3 15h16" stroke="#3E2C23" stroke-width="1.8" stroke-linecap="round"/>'
            '</svg>',
            "logoipsum",
            "",
        ),
        footer_logo(
            '<svg width="22" height="22" viewBox="0 0 22 22" fill="none">'
            '<path d="M11 2l2.2 6H20l-5.1 3.7 1.9 6L11 14l-5.8 3.7 1.9-6L2 8h6.8z" stroke="#3E2C23" stroke-width="1.8" stroke-linejoin="round"/>'
            '</svg>',
            "Logoipsum",
            "",
        ),
        justify="center",
        spacing="8",
        width="100%",
        padding="3rem",
        bg=LIGHT_BG,
        border_radius="24px",
    )


# ─────────────────────────────────────────────
#  INDEX PAGE
# ─────────────────────────────────────────────

def index():
    return rx.box(
        rx.vstack(
            hero_section(),
            benefits_section(),
            featured_section(),
            products_section(),
            categories_section(),
            footer(),
            spacing="8",
            padding_y="2rem",
            width="100%",
        ),
        bg=BACKGROUND,
        width="100%",
        min_height="100vh",
    )


# ─────────────────────────────────────────────
#  LEARN MORE PAGE  (tonos iguales, info relevante)
# ─────────────────────────────────────────────

def lm_navbar():
    """Navbar simplificado para la página interna"""
    return rx.hstack(
        rx.hstack(
            rx.box(
                icon_shimmer_logo(),
                width="36px", height="36px", border_radius="50%", bg=TEXT,
                display="flex", align_items="center", justify_content="center",
            ),
            rx.heading("Shimmer", size="5", color=TEXT, font_weight="bold"),
            spacing="2",
        ),
        rx.hstack(
            rx.link("Home", href="/", color=TEXT, text_decoration="none",
                    font_size="0.85rem", font_weight="500", _hover={"color": PRIMARY}),
            rx.link("About Us", href="/learn-more", color=PRIMARY,
                    text_decoration="none", font_size="0.85rem", font_weight="700"),
            rx.link("Collections", href="/", color=TEXT, text_decoration="none",
                    font_size="0.85rem", font_weight="500", _hover={"color": PRIMARY}),
            rx.link(
                rx.button(
                    "← Back Home",
                    bg=TEXT, color="white", border_radius="999px",
                    font_size="0.78rem", padding_x="1.5rem", padding_y="0.6rem",
                    _hover={"bg": PRIMARY}, transition="all 0.3s ease",
                ),
                href="/", text_decoration="none",
            ),
            spacing="6", align="center",
        ),
        justify="between",
        align="center",
        width="100%",
        padding="1.2rem 3rem",
        bg="white",
        border_radius="999px",
        box_shadow="0 4px 20px rgba(0,0,0,0.08)",
        margin_bottom="3rem",
    )


def stat_box(number, label):
    return rx.vstack(
        rx.heading(number, size="6", color=PRIMARY, font_weight="700"),
        rx.text(label, color=MUTED, font_size="0.82rem", font_weight="500"),
        align="start",
        spacing="1",
    )


def lm_value_card(icon_comp, title, description):
    return rx.vstack(
        rx.box(icon_comp, margin_bottom="0.5rem"),
        rx.heading(title, size="4", color=TEXT, font_weight="600", text_align="center"),
        rx.text(description, color=MUTED, font_size="0.85rem",
                text_align="center", line_height="1.6"),
        align="center",
        spacing="2",
        padding="2rem",
        bg="white",
        border_radius="20px",
        _hover={"transform": "translateY(-4px)", "box_shadow": "0 12px 30px rgba(0,0,0,0.08)"},
        transition="all 0.3s ease",
    )


def learn_more_page():
    return rx.box(
        rx.vstack(
            lm_navbar(),

            # ── HERO ──
            rx.box(
                rx.vstack(
                    rx.text("✦ About Shimmer",
                            color="rgba(255,255,255,0.85)",
                            font_size="0.82rem", font_weight="700",
                            letter_spacing="0.12em"),
                    rx.heading(
                        "The Art Of Fine Jewelry",
                        font_size="4rem",
                        color="white",
                        font_weight="400",
                        line_height="1.1",
                        text_align="center",
                    ),
                    rx.text(
                        "We craft pieces that tell your story — timeless,\nelegant, and made with passion.",
                        white_space="pre-line",
                        color="rgba(255,255,255,0.82)",
                        font_size="1rem",
                        text_align="center",
                        max_width="480px",
                        line_height="1.8",
                    ),
                    rx.link(
                        rx.button(
                            "Shop Our Collection →",
                            bg="white", color=TEXT,
                            border_radius="999px",
                            padding_x="2rem", padding_y="0.85rem",
                            font_size="0.88rem", font_weight="700",
                            _hover={"bg": ACCENT, "color": "white"},
                            transition="all 0.3s ease",
                        ),
                        href="/", text_decoration="none",
                    ),
                    spacing="5",
                    align="center",
                    padding="5rem 2rem",
                ),
                background_image="url('/hero.png')",
                background_size="cover",
                background_position="center",
                border_radius="28px",
                width="100%",
                overflow="hidden",
            ),

            # ── NUESTRA HISTORIA ──
            rx.flex(
                rx.vstack(
                    rx.text("Our Story", color=PRIMARY,
                            font_size="0.78rem", font_weight="700",
                            letter_spacing="0.12em"),
                    rx.heading(
                        "Crafted With Love\nSince 2010",
                        white_space="pre-line",
                        font_size="2.8rem", color=TEXT,
                        font_weight="400", line_height="1.15",
                    ),
                    rx.text(
                        "Shimmer was born from a passion for beautiful things. Every piece in our "
                        "collection is handcrafted by skilled artisans who pour their heart into every detail.",
                        color=MUTED, font_size="0.93rem",
                        line_height="1.8", max_width="400px",
                    ),
                    rx.text(
                        "We source only the finest materials — conflict-free diamonds, 18K gold, "
                        "and premium gemstones — to ensure every piece is as ethically made as it is beautiful.",
                        color=MUTED, font_size="0.93rem",
                        line_height="1.8", max_width="400px",
                    ),
                    # Stats
                    rx.grid(
                        stat_box("230K+", "Happy Clients"),
                        stat_box("15+", "Years Experience"),
                        stat_box("50+", "Artisan Designers"),
                        columns="3",
                        spacing="6",
                        padding="2rem",
                        bg=LIGHT_BG,
                        border_radius="20px",
                        width="100%",
                    ),
                    align="start",
                    spacing="5",
                    flex="1",
                ),
                rx.box(
                    rx.image(
                        src="/model.png",
                        width="400px", height="470px",
                        object_fit="cover", border_radius="24px",
                    ),
                    _hover={"transform": "scale(1.02)"},
                    transition="all 0.4s ease",
                ),
                spacing="9",
                align="center",
                width="100%",
            ),

            # ── POR QUÉ ELEGIRNOS ──
            rx.vstack(
                rx.heading("Why Choose Shimmer?",
                           size="7", color=TEXT, font_weight="400",
                           text_align="center"),
                rx.grid(
                    lm_value_card(icon_shipping(), "Free Worldwide Shipping",
                                  "On all orders over $150. Fast, insured and tracked delivery to your door."),
                    lm_value_card(icon_design(), "Exclusive Designs",
                                  "Each piece is one-of-a-kind, crafted by our in-house designers."),
                    lm_value_card(icon_quality(), "Certified Quality",
                                  "Every piece comes with a certificate of authenticity and lifetime guarantee."),
                    lm_value_card(icon_packaging(), "Luxury Packaging",
                                  "Every order arrives in our signature gift box, perfect for gifting."),
                    columns="4",
                    spacing="5",
                    width="100%",
                ),
                spacing="6",
                align="center",
                width="100%",
                bg=LIGHT_BG,
                border_radius="28px",
                padding="4rem 3rem",
            ),

            # ── COLECCIÓN DESTACADA ──
            rx.box(
                rx.vstack(
                    rx.text("Our Pieces", color=MUTED,
                            font_size="0.78rem", font_weight="700",
                            letter_spacing="0.1em"),
                    rx.heading("A Glimpse Of Our Collection",
                               size="7", color=TEXT, font_weight="400",
                               text_align="center"),
                    rx.grid(
                        product_card("/goldearing.png", "Gold Earring", "240.00"),
                        product_card("/diamondring.png", "Diamond Ring", "240.00"),
                        product_card("/necklace.png", "Gold Necklace", "240.00"),
                        columns="3",
                        spacing="5",
                        width="100%",
                    ),
                    rx.link(
                        rx.button(
                            "View Full Collection →",
                            bg=TEXT, color="white",
                            border_radius="999px",
                            padding_x="2.5rem", padding_y="0.9rem",
                            font_size="0.88rem", font_weight="600",
                            _hover={"bg": PRIMARY},
                            transition="all 0.3s ease",
                        ),
                        href="/", text_decoration="none",
                    ),
                    spacing="6",
                    align="center",
                    padding="4rem 3rem",
                ),
                bg="white",
                border_radius="28px",
            ),

            # ── CTA FINAL ──
            rx.box(
                # Overlay oscuro
                rx.box(
                    bg="rgba(62,44,35,0.62)",
                    position="absolute",
                    top="0", left="0", right="0", bottom="0",
                    border_radius="28px",
                    z_index="1",
                ),
                # Contenido encima del overlay
                rx.vstack(
                    rx.heading(
                        "Ready To Find Your\nPerfect Piece?",
                        white_space="pre-line",
                        font_size="3.2rem", color="white",
                        font_weight="400", text_align="center",
                        line_height="1.15",
                    ),
                    rx.text(
                        "Explore our luxury collections and find the jewelry that speaks to your soul.",
                        color="rgba(255,255,255,0.85)",
                        font_size="1rem", text_align="center",
                    ),
                    rx.link(
                        rx.button(
                            "Explore Collections →",
                            bg="white", color=TEXT,
                            border_radius="999px",
                            padding_x="2.5rem", padding_y="1rem",
                            font_size="0.92rem", font_weight="700",
                            _hover={"bg": ACCENT, "color": "white"},
                            transition="all 0.3s ease",
                        ),
                        href="/", text_decoration="none",
                    ),
                    spacing="5",
                    align="center",
                    padding="5rem 3rem",
                    position="relative",
                    z_index="2",
                ),
                background_image="url('/collection.png')",
                background_size="cover",
                background_position="center",
                border_radius="28px",
                width="100%",
                overflow="hidden",
                position="relative",
            ),

            footer(),

            spacing="8",
            padding="2rem 4rem",
            width="100%",
        ),
        bg=BACKGROUND,
        width="100%",
        min_height="100vh",
    )


# ─────────────────────────────────────────────
#  APP
# ─────────────────────────────────────────────

app = rx.App(
    style={
        "font_family": "Georgia, serif",
    }
)

app.add_page(index, title="Shimmer - Luxury Jewelry")
app.add_page(learn_more_page, route="/learn-more", title="About Us - Shimmer Jewelry")