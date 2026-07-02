# AI_USAGE.md

## Entry: [02-07-2026/2:36pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
Act as an expert Python/Django developer. I am building a small Django-based system for an ecommerce platform that recommends the most suitable shipping box for an order based on product dimensions, weight, and box capacity.  here is full context of problem - "We operate an ecommerce platform. When a customer places an order, the warehouse team needs to know which shipping box should be used. Each product has dimensions and weight. Each box has internal dimensions, maximum weight capacity, and cost.

Your task is to design and build a small Django-based system that recommends the most suitable box for an order. "

Please provide the exact, sequential terminal commands (for a Windows environment) to:

1. Create and activate a Python virtual environment.

2. Install Django and Django REST Framework.

3. Initialize a new Django project named 'ecommerce_shipping'.

4. Create a new Django app named 'box_selector'.

5. Freeze the requirements into a requirements.txt file.

Output only the terminal commands with very brief explanations.
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [No]

- **Mistakes the AI Made:** [No Mistakes Made]

- **Verification Steps:** [Commands Works Properly in VSCode Terminal]

---

## Entry: [02-07-2026/2:38pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
This project requires strict tracking of AI usage in an AI_USAGE.md file. Generate a clean Markdown template for this file. It must include the following sections for each prompt I issue during this project:

- AI Tool Used  
- The Prompt Given  
- Output Accepted  
- Output Rejected or Modified  
- Mistakes the AI Made  
- Verification Steps  

Format it cleanly with Markdown headers so I can easily duplicate the block and fill in my logs as we work.
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [No]

- **Mistakes the AI Made:** [No Mistakes Made]

- **Verification Steps:** [AI_USAGE.md template generated successfully]

---

## Entry: [02-07-2026/2:45pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
Act as an expert Django developer. I need to define two models in my 'box_selector' app for an ecommerce system: `Product` and `Box`.

1. `Product`: fields for name, length, width, height, and weight.

2. `Box`: fields for name, internal_length, internal_width, internal_height, max_weight_capacity, and cost.

Write the exact `models.py` code. Use `FloatField` or `DecimalField` for the dimensions and weight to handle precision properly. Include a `__str__` method for both models to make them easily identifiable in the Django admin panel. After generating the code, provide the exact terminal commands to make and apply the database migrations. I provided you My folder structure and terminal paths "(venv) PS C:\all codes\Desktop\Box_Selection_System\ecommerce_shipping> "as well.
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [No]

- **Mistakes the AI Made:** [No Mistakes Made]

- **Verification Steps:** [Created models.py successfully and migrations worked properly]

---

## Entry: [02-07-2026/2:55pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
I need to write the core 3D bin-packing selection algorithm in a new file called `services.py` inside the 'box_selector' app. Write a function called `get_best_box_for_product(product)`.

The logic must follow these exact steps:

1. Query all `Box` objects where the `max_weight_capacity` is greater than or equal to the `product.weight`.

2. Check if the product's dimensions fit within the box's internal dimensions. Because a product can be rotated in 3D space, you must sort the dimensions of both the product (length, width, height) and the box (internal_length, internal_width, internal_height) from smallest to largest before comparing them.

3. From the boxes that successfully fit the product, order them by `cost` (ascending).

4. Return the cheapest `Box` object.

5. Return `None` if no boxes fit.

Provide the most Pythonic and optimized code for this logic.
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [No]

- **Mistakes the AI Made:** [No Mistakes Made]

- **Verification Steps:** [Implemented services.py and algorithm logic verified manually]

---

## Entry: [02-07-2026/3:05pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
I want to verify the 3D spatial rotation logic in the get_best_box_for_product function you just wrote.

Write a quick, standalone Python script (that does not require Django or the database) that inputs a dummy product with dimensions [10, 5, 2] and a weight of 1kg.

Test it against a dummy box with internal dimensions [5, 12, 3] and a max weight of 5kg.

Print the sorted dimensions of both, and print a boolean confirming whether the logic correctly identifies that the product fits.
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [No]

- **Mistakes the AI Made:** [No Mistakes Made]

- **Verification Steps:** [Executed standalone Python script and verified output correctly]

---

## Entry: [02-07-2026/3:25pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
Now, I need to create an API endpoint using Django REST Framework that accepts a Product ID and returns the best Box using the service function we just wrote.

Please provide the code for three files:

1. `serializers.py`: Write basic ModelSerializers for both `Product` and `Box`.

2. `views.py`: Write an API view (using `@api_view` or `APIView`) that takes a `product_id` in the URL. It should fetch the Product, pass it to my `get_best_box_for_product` function, and return the recommended Box details (and its cost) in a 200 JSON response. If the product doesn't exist, return a 404. If no box fits, return a 400 or 404 with a clean JSON error message.

3. `urls.py`: Show me the URL routing configuration to wire up this endpoint in the 'box_selector' app.
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [No]

- **Mistakes the AI Made:** [No Mistakes Made]

- **Verification Steps:** [Created serializers.py, views.py, urls.py and API endpoint configured successfully]

---

## Entry: [02-07-2026/4:40pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
okay what to do next ? and how can i test ?
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [No]

- **Mistakes the AI Made:** [No Mistakes Made]

- **Verification Steps:** [Added dummy data in database and tested API using browser and terminal]

---

## Entry: [02-07-2026/5:30pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
now i want to setup a superuser
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [No]

- **Mistakes the AI Made:** [No Mistakes Made]

- **Verification Steps:** [Created Django superuser and registered models in admin.py successfully]

---

## Entry: [02-07-2026/6:40pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
after running server i got error, Kindly fix - "(venv) PS C:\all codes\Desktop\Box_Selection_System\ecommerce_shipping> python manage.py runserver

Watching for file changes with StatReloader

Performing system checks...

System check identified no issues (0 silenced).

July 02, 2026 - 15:40:22

Django version 6.0.6, using settings 'ecommerce_shipping.settings'

Starting development server at http://127.0.0.1:8000/

Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.

[02/Jul/2026 15:40:28] "GET /api/box-selector/recommend-box/1 HTTP/1.1" 301 0

django.template.exceptions.TemplateDoesNotExist: rest_framework/api.html"
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [No]

- **Mistakes the AI Made:** [Missed adding 'rest_framework' in INSTALLED_APPS initially]

- **Verification Steps:** [Added rest_framework in settings.py and confirmed API endpoint worked successfully]

---

## Entry: [02-07-2026/7:05pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
Act as an expert QA engineer for Python and Django. I need to write comprehensive unit tests for the Django box selection API I just built in `box_selector/tests.py`.

Generate standard Django `TestCase` classes that test both the `get_best_box_for_product` service function directly, and the REST API endpoint response.

You must include these specific edge cases:

1. A product fits perfectly (product dimensions match box internal dimensions exactly).

2. A product requires 3D rotation to fit (e.g., product L=10, W=5, H=2 fits in Box L=5, W=10, H=2).

3. A product fits the dimensions but is too heavy for all available boxes.

4. A product fits in multiple valid boxes, but the algorithm must successfully choose the cheapest one.

5. A product does not fit in any box due to being too large.

Write the complete, executable test code. Use Django's `APIClient` to test the endpoint.
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [Minor manual adjustments in test file]

- **Mistakes the AI Made:** [No major mistakes]

- **Verification Steps:** [Executed python manage.py test box_selector and verified all test cases passed successfully]

---

## Entry: [02-07-2026/7:20pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
Act as a DevOps engineer. I need to set up a simple GitHub Actions workflow for my Django project to automate my test suite and provide a test output link for a submission.

Generate the YAML code for a workflow file.

The workflow should:

1. Trigger on pushes and pull requests to the `main` branch.

2. Use an `ubuntu-latest` runner.

3. Set up Python 3.10.

4. Install dependencies from `requirements.txt`.

5. Run the database migrations (`python manage.py makemigrations` and `python manage.py migrate`).

6. Execute the Django test suite (`python manage.py test`).

Provide only the YAML configuration and briefly explain where to save this file in my repository.
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [No]

- **Mistakes the AI Made:** [No Mistakes Made]

- **Verification Steps:** [Created GitHub Actions workflow file and verified workflow syntax]

---

## Entry: [02-07-2026/7:35pm]-----------------------------------------------------------------------------------------------------

- **AI Tool Used:** [ Gemini 3 Pro ]

- **The Prompt Given:** > 

[
Act as a Senior Python Developer. Generate a highly professional `README.md` for my Django Box Selector API project.

It must include the following sections formatted cleanly with Markdown:

- Project Overview  
- Tech Stack  
- Setup Instructions  
- Running the Server  
- API Reference  
- Running Tests  
- CI/CD Pipeline  

Do NOT write a "What Did I Learn" section. Leave a placeholder for me to write it manually. write a detailed md from setting up including all the commands
]

- **Output Accepted:** [Yes]

- **Output Rejected or Modified:** [README updated manually according to project structure]

- **Mistakes the AI Made:** [Formatting corrections needed]

- **Verification Steps:** [README.md created successfully and checked locally]

---