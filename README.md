## Generating a Scalable Tracking Number(a unique number)

### API Endpoint Documentation

#### 1. Create Tracked Order

- **Path:** `/create/`
- **Method:** GET, POST
- **Description:** 
  - Allows creation or update of a tracked order.
  - GET: Renders a form to create a new tracked order.
  - POST: Submits form data to create or update a tracked order based on input.
- **Returns:** 
  - If successful, renders the `create_tracked_order.html` template with the form and tracking number.
  - If invalid form data is submitted, redisplays the form with validation errors.

#### 2. Track Order

- **Path:** `/track/<uuid:tracking_number>/`
- **Method:** GET
- **Description:** 
  - Retrieves and displays details of a tracked order identified by `tracking_number`.
- **Returns:** 
  - Renders the `track_order.html` template with details of the tracked order.
  - Returns a 404 page if the `tracking_number` does not correspond to any existing tracked order.

