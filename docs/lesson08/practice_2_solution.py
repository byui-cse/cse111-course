def main():
    sampled_list = [
        "Blue Spruce", "Engelmann Spruce", "Red Alder", "Blue Spruce",
        "Douglas Fir", "Black Hawthorn", "Engelmann Spruce", "Black Hawthorn",
        "Western Larch", "Mountain Hemlock", "Mountain Mahogany", "Blue Spruce",
        "Paper Birch", "Engelmann Spruce", "Douglas Fir", "Western White Pine",
        "Western Larch", "Black Hawthorn", "Limber Pine", "Grand Fir",
        "Mountain Hemlock", "Grand Fir", "Lodgepole Pine", "Western Hemlock",
        "Western Serviceberry", "Douglas Fir", "Whitebark Pine", "Chokecherry",
        "Black Cottonwood", "Quaking Aspen", "Douglas Fir", "Blue Spruce",
        "Ponderosa Pine", "Red Alder", "Black Cottonwood", "Douglas Fir",
        "Ponderosa Pine", "Water Birch", "Limber Pine", "Western Serviceberry",
        "Grand Fir", "Mountain Hemlock", "Water Birch", "Ponderosa Pine",
        "Chokecherry", "Limber Pine", "Western Serviceberry", "Western Larch",
        "Red Alder", "Western Red Cedar", "Western Red Cedar", "Grand Fir",
        "Engelmann Spruce", "Grand Fir", "Western Red Cedar", "Western Hemlock",
        "Western Larch", "Limber Pine", "Quaking Aspen", "Limber Pine",
        "Chokecherry", "Red Alder", "Water Birch", "Rocky Mountain Juniper",
        "Western Hemlock", "Lodgepole Pine", "Whitebark Pine", "Black Hawthorn",
        "Blue Spruce", "Mountain Hemlock", "Chokecherry", "Paper Birch",
        "Limber Pine", "Black Cottonwood", "Chokecherry", "Engelmann Spruce",
        "Black Hawthorn", "Subalpine Fir", "Ponderosa Pine", "Blue Spruce",
        "Blue Spruce", "Douglas Fir", "Paper Birch", "Mountain Mahogany",
        "Mountain Mahogany", "Paper Birch", "Red Alder", "Limber Pine",
        "Red Alder", "Blue Spruce", "Paper Birch", "Western White Pine",
        "Blue Spruce", "Western Larch", "Black Hawthorn", "Ponderosa Pine",
        "Limber Pine", "Western Larch", "Western Serviceberry", "Red Alder",
        "Western White Pine", "Grand Fir", "Engelmann Spruce", "Douglas Fir",
        "Engelmann Spruce", "Paper Birch", "Western Larch", "Limber Pine",
        "Ponderosa Pine", "Douglas Fir", "Paper Birch", "Limber Pine",
        "Subalpine Fir", "Mountain Hemlock", "Western White Pine", "Grand Fir",
        "Blue Spruce", "Black Cottonwood", "Paper Birch", "Water Birch",
        "Grand Fir", "Western Serviceberry", "Limber Pine", "Quaking Aspen",
        "Mountain Hemlock", "Ponderosa Pine", "Western White Pine", "Grand Fir",
        "Water Birch", "Grand Fir", "Mountain Mahogany", "Water Birch",
        "Western White Pine", "Blue Spruce", "Paper Birch", "Ponderosa Pine",
        "Lodgepole Pine", "Western Hemlock", "Blue Spruce", "Red Alder",
        "Quaking Aspen", "Quaking Aspen", "Mountain Hemlock", "Water Birch",
        "Engelmann Spruce", "Grand Fir", "Grand Fir", "Rocky Mountain Juniper",
        "Red Alder", "Whitebark Pine", "Engelmann Spruce", "Mountain Hemlock",
        "Western Larch", "Mountain Mahogany", "Whitebark Pine", "Paper Birch",
        "Rocky Mountain Juniper", "Red Alder", "Grand Fir", "Black Hawthorn",
        "Chokecherry", "Red Alder", "Blue Spruce", "Rocky Mountain Juniper",
        "Grand Fir", "Western Larch", "Western Larch", "Whitebark Pine",
        "Water Birch", "Limber Pine", "Black Cottonwood", "Engelmann Spruce",
        "Grand Fir", "Mountain Mahogany", "Mountain Hemlock", "Paper Birch",
        "Subalpine Fir", "Whitebark Pine", "Limber Pine", "Lodgepole Pine",
        "Ponderosa Pine", "Black Cottonwood", "Whitebark Pine", "Douglas Fir",
        "Paper Birch", "Blue Spruce", "Whitebark Pine", "Black Cottonwood",
        "Western Red Cedar", "Black Hawthorn", "Chokecherry", "Blue Spruce",
        "Whitebark Pine", "Western Hemlock", "Douglas Fir", "Subalpine Fir",
        "Red Alder", "Black Cottonwood", "Western Hemlock", "Engelmann Spruce"
    ]

    # Above is a list of trees that a forest ranger observed in Idaho.
    # Write Python code to count how many of each type of tree the
    # ranger observed. Hint: use a dictionary to store a count of each
    # type of tree.

    # Create an empty dictionary that stores the counters.
    counter_dict = {}

    for species in sampled_list:
        if species not in counter_dict:
            # The current species of tree is NOT in the counter
            # dictionary which means this is the first time the computer
            # has encountered the current species. Add the current
            # species with a count of 1 to the counter dictionary.
            counter_dict[species] = 1
        else:
            # The current species of tree is in the counter dictionary
            # so add 1 to the counter for the current species.
            counter_dict[species] += 1

    for species, count in counter_dict.items():
        print(species, count)


if __name__ == "__main__":
    main()
