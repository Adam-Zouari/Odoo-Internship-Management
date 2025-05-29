#!/bin/bash
# Installation Script for Odoo Stage Management Module

# --- IMPORTANT --- 
# This script provides instructions. Manual steps are usually required.

# 1. Identify your Odoo addons path.
#    This is typically specified in your Odoo configuration file (e.g., /etc/odoo/odoo.conf)
#    or passed as a command-line argument when starting Odoo.
#    Let's assume your addons path is /path/to/your/odoo/addons
ADDONS_PATH="/path/to/your/odoo/addons"

# 2. Define the source directory of the module.
#    This is the directory containing this script and the module code.
MODULE_SOURCE_DIR="/home/ubuntu/odoo_internship/Odoo-Internship-Management-main"

# 3. Define the desired technical name for the module directory.
#    Based on previous discussions and Odoo conventions, use underscores.
MODULE_TECHNICAL_NAME="stage_management"

# --- Instructions --- 

echo "-----------------------------------------------------"
echo "Odoo Stage Management Module Installation Instructions"
echo "-----------------------------------------------------"

echo "1. Ensure your Odoo server is stopped."

echo "2. Rename the module directory if necessary:"
echo "   Current directory: ${MODULE_SOURCE_DIR}"
echo "   Target technical name: ${MODULE_TECHNICAL_NAME}"
echo "   If the current directory name is not ${MODULE_TECHNICAL_NAME}, please rename it."
echo "   Example: mv ${MODULE_SOURCE_DIR} /path/to/${MODULE_TECHNICAL_NAME}"

echo "3. Copy the module directory (${MODULE_TECHNICAL_NAME}) to your Odoo addons path:"
echo "   Target addons path: ${ADDONS_PATH}"
echo "   Example command: cp -r /path/to/${MODULE_TECHNICAL_NAME} ${ADDONS_PATH}/"

echo "4. Set correct file permissions for the Odoo user (if necessary):"
echo "   Example command: chown -R odoo:odoo ${ADDONS_PATH}/${MODULE_TECHNICAL_NAME}"
echo "   Example command: chmod -R 755 ${ADDONS_PATH}/${MODULE_TECHNICAL_NAME}"

echo "5. Restart your Odoo server."
echo "   Important: Update the module list and install/upgrade the module."
echo "   You can do this by starting Odoo with the '-u' flag:"
echo "   Example: ./odoo-bin -c /etc/odoo/odoo.conf -u ${MODULE_TECHNICAL_NAME}"
echo "   Alternatively, go to Apps -> Update Apps List -> Find 'Stage Management' and click Install/Upgrade."

echo "-----------------------------------------------------"
echo "Installation instructions complete."
echo "-----------------------------------------------------"

exit 0

