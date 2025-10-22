# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Last Page is a Python-based web application designed to create custom covers for devices such as Kindles. The application is built using FastAPI and is in early development.

## Technology Stack

- **Python**: 3.14 (specified in `.python-version`)
- **Framework**: FastAPI with standard extras
- **Package Manager**: uv (manages dependencies via `pyproject.toml` and `uv.lock`)
- **Settings Management**: pydantic-settings

## Development Commands

### Running the Application

```bash
fastapi dev main.py
```

This starts the FastAPI development server with hot reload enabled.

### Installing Dependencies

```bash
uv sync
```

### Adding New Dependencies

```bash
uv add <package-name>
```

## Project Structure

The project is currently in a minimal state with a single-file application:

- `main.py`: Contains the FastAPI application with three endpoints:
  - `GET /`: Returns a hello message
  - `GET /health`: Health check endpoint
  - `POST /create-cover`: Placeholder for cover creation functionality (currently returns empty response)

## Architecture Notes

- The application is a straightforward FastAPI app without modular structure yet
- The main cover creation feature (`/create-cover` endpoint) is currently a stub and needs implementation
- No tests, configuration management, or service layer structure exists yet
