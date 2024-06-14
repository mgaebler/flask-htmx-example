from typing import List, Dict, Any

# Define the type for a single dataset
DatasetType = Dict[str, Any]

# Create the array of data
fruit_data: List[DatasetType] = [
    {
        "name": "Apple",
        "slug": "apple",
        "description": "A sweet, crunchy fruit that comes in various colors like red, green, and yellow.",
        "tags": ["sweet", "crunchy", "juicy"]
    },
    {
        "name": "Banana",
        "slug": "banana",
        "description": "A long, yellow fruit that is soft and sweet when ripe, commonly eaten as a snack.",
        "tags": ["sweet", "soft", "snack"]
    },
    {
        "name": "Cherry",
        "slug": "cherry",
        "description": "A small, round fruit that is typically red or black, known for its sweet and tart flavor.",
        "tags": ["sweet", "tart", "small"]
    }
]
