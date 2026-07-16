from rich import print as p

p("[bold yellow]Welcome to the West Bengal Holiday Planner![/]")
season = input("Enter your season (summer, monsoon, or winter): ").strip().lower()

if season == "summer":
    trip_type = input("Do you want a beach, hill, city, or wildlife trip? ").strip().lower()

    if trip_type == "beach":
        p("[yellow]Go to[/] [blue]Digha[/] or [green]New Digha[/] in West Bengal.")
    elif trip_type == "hill":
        p("[yellow]Go to[/] [blue]Darjeeling[/] or [green]Kalimpong[/] in West Bengal.")
    elif trip_type == "city":
        p("[yellow]Go to[/] [blue]Kolkata[/] or [green]Howrah[/] in West Bengal.")
    elif trip_type == "wildlife":
        p("[yellow]Go to[/] [blue]Sundarbans[/] or [green]Buxa[/] in West Bengal.")
    else:
        p("[red]Please choose beach, hill, city, or wildlife.[/]")

elif season == "monsoon":
    trip_type = input("Do you want a hill, forest, or city trip? ").strip().lower()

    if trip_type == "hill":
        p("[yellow]Go to[/] [blue]Darjeeling[/] or [green]Kalimpong[/] in West Bengal.")
    elif trip_type == "forest":
        p("[yellow]Go to[/] [blue]Dooars[/] or [green]Jaldapara[/] in West Bengal.")
    elif trip_type == "city":
        p("[yellow]Go to[/] [blue]Kolkata[/] or [green]Bishnupur[/] in West Bengal.")
    else:
        p("[red]Please choose hill, forest, or city.[/]")

elif season == "winter":
    trip_type = input("Do you want a beach, hill, heritage, or wildlife trip? ").strip().lower()

    if trip_type == "beach":
        p("[yellow]Go to[/] [blue]Mandarmani[/] or [green]Digha[/] in West Bengal.")
    elif trip_type == "hill":
        p("[yellow]Go to[/] [blue]Darjeeling[/] or [green]Mirik[/] in West Bengal.")
    elif trip_type == "heritage":
        p("[yellow]Go to[/] [blue]Bishnupur[/] or [green]Murshidabad[/] in West Bengal.")
    elif trip_type == "wildlife":
        p("[yellow]Go to[/] [blue]Sundarbans[/] or [green]Jaldapara[/] in West Bengal.")
    else:
        p("[red]Please choose beach, hill, heritage, or wildlife.[/]")

else:
    p("[red]Invalid season. Please enter summer, monsoon, or winter.[/]")