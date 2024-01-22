# Django Project Structure

Welcome to the Django Project Structure Template repository! If you find yourself repeatedly using the same file structure for your Django projects and can't find a suitable template online, you're in the right place. This repository contains my preferred Django project structure, and I'm sharing it with the community in the hope that it might be useful for others too.

## Features

- **Clean Directory Structure:** A well-organized layout for your Django project.
- **Environment Handling:** Includes environment utility (`env_utils.py`) for managing environment variables.
- **Docker Support:** Dockerfile and docker-compose.yaml included for containerization.
- **Poetry Integration:** pyproject.toml for managing project dependencies.
- **Configuration Files:** .env for environment variables and .env.example as a template.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/django-project-structure-template.git
   ```
2. **Create an Environment File:**
   Create a file named .env in the root of your project. Add the following content and replace <DJANGO_SECRET_KEY> with a secure Django secret key:
   DJANGO_SECRET_KEY=<YOUR_SECRET_KEY>
   PROJECT_STATE=development  # Change to 'production' for production environment
3. **Copy the Structure:**
   Copy the desired parts of the project structure into your new Django project.

4. **Customize:**
   Modify the settings and structure to fit your project's specific requirements.

## Building and Running Your Application with Docker

When you're ready, start your application by running:
```bash
docker compose up --build
```

Your application will be available at http://localhost:8000.

### Deploying Your Application to the Cloud

1. Build your image, e.g., `docker build -t myapp .`.
2. If your cloud uses a different CPU architecture than your development machine (e.g., you are on a Mac M1 and your cloud provider is amd64), build the image for that platform, e.g.:
   ```bash
   docker build --platform=linux/amd64 -t myapp .
   ```
3. Push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/) docs for more detail on building and pushing.

### Contributions

Contributions and feedback are welcome! If you have ideas for improvements or would like to contribute your own variations, feel free to open an issue or create a pull request.

### License

This project is licensed under the MIT License - see the LICENSE file for details.