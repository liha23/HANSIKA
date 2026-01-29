# Contributing to Employee Payroll Management System

Thank you for considering contributing to this project! This document provides guidelines for contributing.

## 🎯 Project Goals

This is an educational project designed to demonstrate:
- Python database connectivity
- MySQL CRUD operations
- Basic payroll management concepts
- Software development best practices

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

1. **Title**: Clear, descriptive title
2. **Description**: Detailed description of the bug
3. **Steps to Reproduce**: 
   - Step 1
   - Step 2
   - Step 3
4. **Expected Behavior**: What should happen
5. **Actual Behavior**: What actually happens
6. **Environment**:
   - OS (Windows/Linux/macOS)
   - Python version
   - MySQL version
7. **Screenshots**: If applicable

### Suggesting Features

Feature suggestions are welcome! Please include:

1. **Feature Description**: What feature you'd like to see
2. **Use Case**: Why this feature would be useful
3. **Possible Implementation**: Ideas on how it could work
4. **Examples**: Examples from other projects (if any)

### Pull Requests

1. **Fork the Repository**
   ```bash
   # Click the Fork button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/HANSIKA.git
   cd HANSIKA
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Write clean, readable code
   - Follow Python PEP 8 style guidelines
   - Add comments for complex logic
   - Test your changes

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add feature: description of your feature"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template

## 📝 Coding Standards

### Python Style Guide

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/):

- Use 4 spaces for indentation (not tabs)
- Keep lines under 80 characters when possible
- Use descriptive variable names
- Add docstrings for functions
- Use snake_case for function and variable names

### Example:

```python
def calculate_total_salary(basic_salary, allowance):
    """
    Calculate total salary from basic salary and allowance.
    
    Args:
        basic_salary (int): Basic salary amount
        allowance (int): Allowance amount
        
    Returns:
        int: Total salary
    """
    return basic_salary + allowance
```

### SQL Best Practices

- Use parameterized queries (already implemented)
- Always commit transactions
- Handle exceptions properly
- Close database connections when done

### Testing

Before submitting:

1. Test all features manually
2. Verify database operations work correctly
3. Check for SQL injection vulnerabilities
4. Test edge cases (invalid input, empty database, etc.)

## 🔍 Code Review Process

1. Maintainers will review your PR
2. They may request changes
3. Make requested changes and push to your branch
4. Once approved, your PR will be merged

## 📋 Commit Message Guidelines

Write clear commit messages:

- Use present tense ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Add detailed description if needed

Examples:
```
Good: Add validation for employee ID input
Bad: fixed stuff
```

## 🐛 Issue Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to documentation
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention is needed

## ✅ Definition of Done

A contribution is considered complete when:

- [ ] Code works as expected
- [ ] No new bugs introduced
- [ ] Code follows style guidelines
- [ ] Documentation is updated (if needed)
- [ ] Changes are tested
- [ ] Commit messages are clear

## 📧 Questions?

If you have questions:
- Open an issue with the `question` label
- Check existing issues first

## 🎓 Learning Resources

- [Python Documentation](https://docs.python.org/3/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Git Tutorial](https://git-scm.com/docs/gittutorial)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

## 📜 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn

Thank you for contributing! 🎉
