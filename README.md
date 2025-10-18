# Odoo Module: Internship Management

## 1. Introduction

This Odoo module aims to provide a comprehensive solution for managing academic internships within a company or educational institution. It allows tracking of students, partner companies, tutors (academic and professional), internship agreements, and associated reports.

## 2. Technical Name

The technical name of the module is `stage_management`. It is crucial to use this name (with an underscore `_`) for the module directory and in all external identifier references (XML IDs) in code and XML files to ensure consistency and avoid errors.

## 3. Dependencies

This module depends on the following standard Odoo modules:

*   `base`: Odoo's base module.
*   `mail`: For tracking (chatter), activities, and notification features.
*   `hr`: Potentially used to link tutors to employees or for other HR features (although direct usage is not explicitly detailed in the provided code, it is listed as a dependency).

Ensure these modules are installed in your Odoo instance.

## 4. Installation

Follow these steps to install the module:

1.  **Stop the Odoo server**.

2.  **Prepare the module directory** :
    *   Ensure the directory containing the module code is named `stage_management` (with an underscore).
    *   If your current directory is different (e.g., `Odoo-Internship-Management-main`), rename it:
        ```bash
        # Example : Replace /path/to/your/module with the actual path
        mv /path/to/your/module/Odoo-Internship-Management-main /path/to/your/module/stage_management
        ```

3.  **Copy the module to the Odoo addons directory:** :
    *   Identify the path to your Odoo addons directory (often defined in your `odoo.conf` file).
    *   Copy the `stage_management` directory to this path:
        ```bash
        # Example: Replace /path/to/your/addons with the actual path
         # and /path/to/your/module with the path where stage_management is located
         cp -r /path/to/your/module/stage_management /path/to/your/addons/
        ```

4.  **Set permissions (if necessary):** :
    *   Ensure the user running the Odoo process has read rights on the module files.
    *   If necessary, adjust the owner and permissions:
        ```bash
         # Example: Replace 'odoo' with the Odoo system user if different
         # and /path/to/your/addons with the actual path
         sudo chown -R odoo:odoo /path/to/your/addons/stage_management
         sudo chmod -R 755 /path/to/your/addons/stage_management
        ```

5.  **Restart the Odoo server**.

6.  **Update the module list and install** :
    *   **Option 1 (Command Line)** : Restart Odoo, updating the module directly (recommended to ensure changes are applied).
        ```bash
        # Example: Adapt the path to odoo-bin and the configuration file
         ./odoo-bin -c ~/.odoo/odoo.conf -d MyDB -u stage_management
        ```
        *If the module was not installed, replace `-u stage_management` with `-i stage_management` on the first startup after copying.*
    *   **Option 2 (Odoo Interface)** :
        *   Enable Developer Mode.
        *   Go to the `Apps` menu.
        *   Click `Update Apps List`.
        *   Search for the `Stage Management` module.
        *   Click `Install` (or `Upgrade` if already installed).

## 5. Configuration

No specific configuration is required after installation for the basic functionality of the module.

## 6.  Main Features

*   **Student Management** (`stage.student`): Recording information about student interns.
*   **Company Management** (`stage.company`): Recording information about companies hosting interns.
*   **Tutor Management** (`stage.tutor`): Distinction between academic and professional tutors.
*   **Internship Management** (`stage.internship`): Complete tracking of internships including dates, student, company, tutors, and state (Draft, In Progress, Completed, Cancelled).
*   **Agreement Generation**: Automatic generation of the internship agreement in PDF format via a QWeb report.
*   **Internship Report Management** (`stage.report`): Tracking of reports submitted by students, with a validation system.
*   **Views and Menus**: Integration into the Odoo interface with dedicated menus and views (list, form, kanban, search) for each model.

## 7. Main Data Models

*   `stage.student`: Student information.
*   `stage.company`: Company information.
*   `stage.tutor`: Tutor information (with academic/professional type).
*   `stage.internship`: Core internship data, linking the other models.
*   `stage.report`: Internship report information.

## 8. Reports

*   **Internship Agreement**: A QWeb report (`stage_management.report_internship_agreement`) is defined to generate the agreement in PDF format.

## 9. Security

Access rights for the different models are defined in the `security/ir.model.access.csv` file. Ensure appropriate user groups have the necessary permissions.

## 10. Recording

https://github.com/user-attachments/assets/e496c1cd-3437-4ea0-bd92-a96f3fc4ff25
