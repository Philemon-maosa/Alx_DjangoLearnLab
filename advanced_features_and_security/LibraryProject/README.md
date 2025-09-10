# LibraryProject

A Django-based library management system that allows users to manage books, authors, and libraries with role-based access control.

---

## Features

- **Book Management**
  - Add, view, edit, and delete books
  - Custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)

- **User Management**
  - Custom user model (`CustomUser`) with profile photo and date of birth
  - Role-based groups: `Admins`, `Editors`, `Viewers`
  - Automatic user profile creation

- **Library and Author Management**
  - Manage libraries and associate books
  - Manage authors and associate books
  - Assign librarians to libraries

- **Permissions Enforcement**
  - Views protected by permissions using Django decorators
  - Only authorized users can perform actions based on roles

---

## Requirements

- Python 3.10+
- Django 5.2.5
- Pillow (for image uploads)

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Philemon-maosa/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/advanced_features_and_security/LibraryProject
