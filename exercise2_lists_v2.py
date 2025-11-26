delivery_routes = [
    "North Track", "East Road", "Southern Line", "Old Street", "West Route",
    "Northern Path", "Central Way", "Main Street", "New Bypass", "Express Route"
]
print("Initial routes:", delivery_routes)

delivery_routes.append("Hill View Lane")
delivery_routes.remove("Old Street")
print("\nUpdated list:", delivery_routes)

delivery_routes.sort()
delivery_routes.reverse()
print("\nRoutes sorted in reverse:", delivery_routes)

routes_starting_with_N = sum(1 for r in delivery_routes if r.startswith("N"))
print("\nCount of routes starting with N:", routes_starting_with_N)

long_names = [r for r in delivery_routes if len(r) > 10]
print("\nRoutes longer than 10 characters:", long_names)
