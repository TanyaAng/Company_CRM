## ARTICLES API

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">API endpoints</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


### About The Project
  JSON REST API application for Company CRM system:
 - allows CRUD operations to a company entites;
 - allows CRUD operations to a employee entites;
 - employees and companies has One-to-Many relationship;
 - provided unittests for models validations;
 - provided integration tests for API views;
  
<p align="right"><a href="#top">back to top</a></p>

#### Build With
* [Django REST Framework](https://www.django-rest-framework.org/)
* [Docker](https://www.docker.com/)

### Getting Started
#### Installation
1. Clone the repo
   ```sh
   https://github.com/TanyaAng/Company_CRM.git
   ```
2. Install all Python libraries
   ```sh
   pip install -r requirements.txt
   ```

<p align="right"><a href="#top">back to top</a></p>

### Usage
1. Docker build - outside of Company_CRM directory
     ```sh
   docker build -f Company_CRM/Dockerfile -t company Company_CRM
   ```
2. Docker compose - inside Company_CRM directory
    ```sh
   docker-compose up -d web
   ```
3. Migrate
    ```sh
   docker-compose run web python manage.py migrate
   ```

<p align="right"><a href="#top">back to top</a></p>

### API endpoints

| Datapoint                   | HTTP Method | Description                |
|-----------------------------|-------------|----------------------------|
| /api/company/               | GET         | get all companies          |
| /api/company                | POST        | create new company entity  |
| /api/company/{company_id}   | GET         | get single company         |
| /api/company/{company_id}   | POST        | update single company      |
| /api/company/{company_id}   | DELETE      | delete single company      |
| /api/employee/              | GET         | get all companies          |
| /api/employee               | POST        | create new employee entity |
| /api/employee/{employee_id} | GET         | get single employee        |
| /api/employee/{employee_id} | POST        | update single employee     |
| /api/employee/{employee_id} | DELETE      | delete single employee     |



<p align="right"><a href="#top">back to top</a></p>

### License
MIT License

<p align="right"><a href="#top">back to top</a></p>

### Contact

Tanya Angelova - [LinkedIn](https://www.linkedin.com/in/tanya-angelova-44b03590/) - t.j.angelova@gmail.com

Project Link: [github link]

<p align="right"><a href="#top">back to top</a></p>

[LinkedIn]: https://www.linkedin.com/in/tanya-angelova-44b03590/
[github link]: https://github.com/TanyaAng/Company_CRM