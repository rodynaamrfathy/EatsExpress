<div align="center">
  <img src="/readmeimages/Logo.png" alt="EatsExpress Logo" width="100%">
</div>

# EatsExpress

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Licensing](#licensing)
- [The Story Behind EatsExpress](#the-story-behind-eatsexpress)
  - [Inspiration](#inspiration)
  - [Technical Challenges](#technical-challenges)
  - [Overcoming Struggles](#overcoming-struggles)
  - [Future Vision](#future-vision)
  - [Detailed Technical Explanation](#detailed-technical-explanation)
- [Landing Page](#landing-page)
- [Contact Us](#contact-us)

## Introduction
EatsExpress is an online food ordering and delivery service that connects users with local restaurants in Egypt. Users can browse various cuisines, place orders, and have their favorite meals delivered right to their doorstep.

[Deployed Site](http://rodyna.pythonanywhere.com)

### Our LinkedIn Accounts
[Rodyna Amr's LinkedIn Profile](https://www.linkedin.com/in/rodyna-amr-22027012cs/) | [Mohammed Yasser's LinkedIn Profile](https://www.linkedin.com/in/mohamed-yasser-42b16a282/) | [Mohammed Essam's LinkedIn Profile](https://www.linkedin.com/in/mohamed-essam-742553279/)

<div align="center">
  <img src="/readmeimages/presentation1.png" alt="presentation" width="100%">
</div>
<div align="center">
  <img src="/readmeimages/presentation2.png" alt="presentation" width="100%">
</div>
<div align="center">
  <img src="/readmeimages/presentation3.png" alt="presentation" width="100%">
</div>
<div align="center">
  <img src="/readmeimages/presentation4.png" alt="presentation" width="100%">
</div>
<div align="center">
  <img src="/readmeimages/presentation5.png" alt="presentation" width="100%">
</div>
<div align="center">
  <img src="/readmeimages/presentation6.png" alt="presentation" width="100%">
</div>

## Installation
To get a local copy up and running, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/rodynaamrfathy/EatsExpress
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Set up the database:
    ```sh
    flask db upgrade
    ```
4. Run the application:
    ```sh
    python run.py
    ```

## Usage
1. Open your browser and go to `http://localhost:5000`.
2. Register a new account or log in if you already have one.
3. Browse through the list of available restaurants and select your desired meals.
4. Add items to your cart and proceed to checkout.
5. Track your order in real-time until it gets delivered.

## Contributing
Contributions are what make the open-source community such an amazing place to be, learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch:
    ```sh
    git checkout -b feature/AmazingFeature
    ```
3. Commit your Changes:
    ```sh
    git commit -m 'Add some AmazingFeature'
    ```
4. Push to the Branch:
    ```sh
    git push origin feature/AmazingFeature
    ```
5. Open a Pull Request.

## Licensing
Distributed under the MIT License. See `LICENSE` for more information.

---

## The Story Behind EatsExpress

### Inspiration
The inspiration behind EatsExpress came from the need to provide a convenient and efficient way for people to order food online, especially during the COVID-19 pandemic when going out was not always an option. The idea was to create a platform that not only connects users with a variety of local restaurants but also ensures timely delivery and a seamless user experience.

### Technical Challenges
One of the significant technical challenges was building a clean Flask web app architecture and connecting the web static with the storage file. We learned everything by doing it, which gave us the experience, but also a lot of sleepless nights.

![Sleepless nights](readmeimages/sleepy.webp) 

### Overcoming Struggles
During the development process, there were moments of struggle, particularly with doing updates and adding features to improve and give users a better experience. We also faced challenges in designing a user-friendly interface that caters to both tech-savvy users and those who are less familiar with technology.

### Future Vision
In the next iteration, we envision adding more features such as a rewards system for frequent users, AI-powered restaurant recommendations, and integration with more payment gateways to offer greater flexibility. We also plan to expand our service area to cover more cities and regions.

### Detailed Technical Explanation
The backend of EatsExpress is built with Flask, a lightweight WSGI web application framework in Python. The database is managed using SQLAlchemy and JSON.

Here's an example of the code used for handling order tracking:
```python
@app.route('/track_order/<order_id>')
def track_order(order_id):
    """
    Route to track the status of an order.

    Parameters:
        order_id (str): The ID of the order to track.

    Returns:
        Renders the order tracking page or redirects to account details if order not found.
    """
    order = storage.get(Order, order_id)
    if not order:
        flash('Order not found.', 'danger')
        return redirect(url_for('accountdetails'))

    # Calculate if the order should be marked as delivered
    if order.status == "out for delivery":
        delivery_time_elapsed = (datetime.utcnow() - order.updated_at).total_seconds() / 60  # in minutes
        if float(delivery_time_elapsed) > float(convert_to_float(order.delivery_time)):
            order.status = "delivered"
            storage.save()

    return render_template('track_order.html', order=order, title="Track Order")
```

## Landing Page
https://me8624708.wixsite.com/eat-express

## Contact Us

For any questions, feedback, or support inquiries, please feel free to reach out to our team:

<h2>Email:</h2>

- rodynaamr@icloud.com
- me8624708@gmail.com
- mohamedyasser192023@gmail.com
