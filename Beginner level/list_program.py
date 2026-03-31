justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Initial List:", justice_league)

# Add members
justice_league.append("Batgirl")
justice_league.append("Nightwing")

# Move Wonder Woman to front
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

# Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]

# Sort
justice_league.sort()

print("Final List:", justice_league)