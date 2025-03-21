# XGC Theme App

**Version:** 1.0.0  
**Copyright:** © 2025 XGC Software Inc.  
**License:** Proprietary  MIT

---

## Overview

The **XGC Theme App** is a custom Frappe application designed to integrate the **OneUI Vue Edition** template into the Frappe framework. This app provides a modern, responsive, and feature-rich user interface for Frappe-based applications. It includes updates to Laravel 12, Vue.js, and other dependencies as of March 6, 2025.

---

## Features

- **OneUI Vue Edition Integration**: A sleek and modern UI template for Frappe.
- **Laravel 12 Support**: Updated to the latest Laravel version for enhanced performance and security.
- **Vue.js 3**: Utilizes the latest Vue.js features for a dynamic and responsive frontend.
- **Customizable Layouts**: Includes reusable layout components for backend and frontend pages.
- **Pre-configured Dependencies**: Includes updated versions of popular libraries like CKEditor, Chart.js, SweetAlert2, and more.

---

## Installation

### Prerequisites

1. **Frappe Bench**: Ensure you have Frappe Bench installed and set up.
2. **Node.js**: Install Node.js (LTS version recommended).
3. **Python**: Ensure Python 3.7+ is installed.

### Steps

1. **Create a New Frappe App**  
   Run the following command to create a new Frappe app:

   ```bash
   bench new-app xgc_theme_app
   ```

2. **Install the App on a Site**  
   Install the app on your Frappe site:

   ```bash
   bench --site your_site_name install-app xgc_theme_app
   ```

3. **Copy OneUI Files**  
   Copy the OneUI Vue Edition files into the `xgc_theme_app/public` directory. Ensure the following folders are included:

   - `src/assets/`
   - `src/components/`
   - `src/layouts/`
   - `src/views/`
   - `public/assets/`

4. **Update Frappe Assets**  
   Link the OneUI assets to Frappe by updating the `hooks.py` file in the `xgc_theme_app` directory:

   ```python
   from frappe import _

   def get_assets(app):
       return {
           "xgc_theme_app": {
               "public": [
                   "public/css/oneui.css",
                   "public/js/oneui.app.min.js"
               ]
           }
       }
   ```

5. **Build Assets**  
   Build the assets using the following command:

   ```bash
   bench build
   ```

6. **Restart Frappe**  
   Restart the Frappe server to apply the changes:

   ```bash
   bench restart
   ```

---

## Configuration

### Customizing the Theme

1. **Sass Variables**  
   Customize the theme by modifying the Sass variables in `src/assets/scss/custom/_variables.scss`.

2. **Layouts**  
   Update the layout files in `src/layouts/` to match your application's requirements.

3. **Components**  
   Add or modify components in `src/components/` as needed.

### Updating Dependencies

To update dependencies, run:

```bash
npm install
```

---

## Usage

### Layouts

- **Backend Layout**: Use `Backend.vue` for admin and backend pages.
- **Frontend Layout**: Use `Simple.vue` for landing pages and public-facing content.

### Components

- **BaseBlock**: Use for structured content blocks.
- **BaseNavigation**: Use for sidebar navigation.
- **BasePageHeading**: Use for page headings with titles and subtitles.

### Plugins

- **CKEditor**: Use for rich text editing.
- **Chart.js**: Use for data visualization.
- **SweetAlert2**: Use for alerts and notifications.

---

## Updates

OneUI Vue Edition will receive free updates in the future. To update the theme:

1. Download the latest version of OneUI Vue Edition.
2. Replace the existing files in `xgc_theme_app/public` with the new files.
3. Rebuild the assets:

   ```bash
   bench build
   ```

4. Restart the Frappe server:

   ```bash
   bench restart
   ```

---

## Credits

- **OneUI Vue Edition**: A powerful and flexible Vue.js template.
- **Frappe Framework**: A full-stack web framework for building modern applications.
- **XGC Software Inc.**: For the development and customization of the XGC Theme App.

---

## Support

For support, contact **XGC Software Inc.** at [support@xgcsoftware.com](mailto:support@xgcsoftware.com).

---

## License

This project is proprietary software owned by **XGC Software Inc.** Unauthorized use, reproduction, or distribution is strictly prohibited.

---

## Thank You

Thank you for choosing the **XGC Theme App**! We hope it enhances your Frappe-based projects and provides a seamless development experience.

---

This README provides a comprehensive guide for installing, configuring, and using the **XGC Theme App** with the **OneUI Vue Edition** template. Let me know if you need further assistance!