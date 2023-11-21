from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ComponentsView(LoginRequiredMixin,TemplateView):
    pass

# bootstrap-ui

bootstrap_ui_alerts_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-alerts.html")
bootstrap_ui_badges_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-badge.html")
bootstrap_ui_buttons_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-buttons.html")
bootstrap_ui_cards_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-cards.html")
bootstrap_ui_dropdowns_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-dropdowns.html")
bootstrap_ui_navs_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-navs.html")
bootstrap_ui_accordions_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-tabs-accordions.html")
bootstrap_ui_modals_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-modals.html")
bootstrap_ui_images_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-images.html")
bootstrap_ui_progress_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-progressbars.html")
bootstrap_ui_paginations_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-pagination.html")
bootstrap_ui_popover_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-popover-tooltips.html")
bootstrap_ui_spinner_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-spinner.html")
bootstrap_ui_carousel_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-carousel.html")
bootstrap_ui_video_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-video.html")
bootstrap_ui_typography_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-typography.html")
bootstrap_ui_grid_view = ComponentsView.as_view(template_name = "components/bootstrap-ui/ui-grid.html")

# advance-ui
advance_ui_alertify_view = ComponentsView.as_view(template_name = "components/advance-ui/advanced-alertify.html")
advance_ui_ratings_view = ComponentsView.as_view(template_name = "components/advance-ui/advanced-ratings.html")
advance_ui_nestable_view = ComponentsView.as_view(template_name = "components/advance-ui/advanced-nestable.html")
advance_ui_rangeslider_view = ComponentsView.as_view(template_name = "components/advance-ui/advanced-rangeslider.html")
advance_ui_sweet_alert_view = ComponentsView.as_view(template_name = "components/advance-ui/advanced-sweet-alert.html")
advance_ui_lightbox_view = ComponentsView.as_view(template_name = "components/advance-ui/advanced-lightbox.html")

# icons
icons_materialdesign_view = ComponentsView.as_view(template_name = "components/icons/icons-materialdesign.html")
icons_dripicons_view = ComponentsView.as_view(template_name = "components/icons/icons-dripicons.html")
icons_fontawesome_view = ComponentsView.as_view(template_name = "components/icons/icons-fontawesome.html")
icons_themify_view = ComponentsView.as_view(template_name = "components/icons/icons-themify.html")
icons_unicons_view = ComponentsView.as_view(template_name = "components/icons/icons-unicons.html")

# tables
tables_basic_view = ComponentsView.as_view(template_name = "components/tables/tables-basic.html")
tables_datatable_view = ComponentsView.as_view(template_name = "components/tables/tables-datatable.html")
tables_responsive_view = ComponentsView.as_view(template_name = "components/tables/tables-responsive.html")
tables_editable_view = ComponentsView.as_view(template_name = "components/tables/tables-editable.html")

# forms
forms_elements_view = ComponentsView.as_view(template_name = "components/forms/form-elements.html")
forms_validation_view = ComponentsView.as_view(template_name = "components/forms/form-validation.html")
forms_advanced_view = ComponentsView.as_view(template_name = "components/forms/form-advanced.html")
forms_editors_view = ComponentsView.as_view(template_name = "components/forms/form-editors.html")
forms_file_uploads_view = ComponentsView.as_view(template_name = "components/forms/form-uploads.html")
forms_mask_view = ComponentsView.as_view(template_name = "components/forms/form-mask.html")
forms_summernote_view = ComponentsView.as_view(template_name = "components/forms/form-summernote.html")

# charts
charts_morris_view = ComponentsView.as_view(template_name = "components/charts/charts-morris.html")
charts_apex_view = ComponentsView.as_view(template_name = "components/charts/charts-apex.html")
charts_chartist_view = ComponentsView.as_view(template_name = "components/charts/charts-chartist.html")
charts_chartjs_view = ComponentsView.as_view(template_name = "components/charts/charts-chartjs.html")
charts_flot_view = ComponentsView.as_view(template_name = "components/charts/charts-flot.html")
charts_sparkline_view = ComponentsView.as_view(template_name = "components/charts/charts-sparkline.html")
charts_knob_view = ComponentsView.as_view(template_name = "components/charts/charts-knob.html")

# maps
maps_google_view = ComponentsView.as_view(template_name = "components/maps/maps-google.html")
maps_vector_view = ComponentsView.as_view(template_name = "components/maps/maps-vector.html")

# layouts
layouts_horizontal = ComponentsView.as_view(template_name="components/layouts/layouts-horizontal.html")
layouts_dark_sidebar = ComponentsView.as_view(template_name="components/layouts/layouts-dark-sidebar.html")
layouts_small_sidebar = ComponentsView.as_view(template_name="components/layouts/layouts-sidebar-sm.html")
layouts_icon_sidebar = ComponentsView.as_view(template_name="components/layouts/layouts-icon-sidebar.html")
layouts_colored_sidebar = ComponentsView.as_view(template_name="components/layouts/layouts-colored-sidebar.html")
layouts_boxed_sidebar = ComponentsView.as_view(template_name="components/layouts/layouts-boxed.html")