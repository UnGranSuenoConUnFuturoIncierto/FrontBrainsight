from django.urls import path
from components.views import (
    
  # bootstrap-ui
  bootstrap_ui_alerts_view,
  bootstrap_ui_badges_view,
  bootstrap_ui_buttons_view,
  bootstrap_ui_cards_view,
  bootstrap_ui_dropdowns_view,
  bootstrap_ui_navs_view,
  bootstrap_ui_accordions_view,
  bootstrap_ui_modals_view,
  bootstrap_ui_images_view,
  bootstrap_ui_progress_view,
  bootstrap_ui_paginations_view, 
  bootstrap_ui_popover_view,
  bootstrap_ui_spinner_view,
  bootstrap_ui_carousel_view,
  bootstrap_ui_video_view,
  bootstrap_ui_typography_view,
  bootstrap_ui_grid_view,
  
  # advance-ui
  advance_ui_alertify_view,
  advance_ui_ratings_view,
  advance_ui_nestable_view,
  advance_ui_rangeslider_view,
  advance_ui_sweet_alert_view,
  advance_ui_lightbox_view,
 
  # icons
  icons_materialdesign_view,
  icons_dripicons_view,
  icons_fontawesome_view,
  icons_themify_view,
  icons_unicons_view,

  # table
  tables_basic_view,
  tables_datatable_view,
  tables_responsive_view,
  tables_editable_view,
  
  # forms
  forms_elements_view,
  forms_validation_view,
  forms_advanced_view,
  forms_editors_view,
  forms_file_uploads_view,
  forms_mask_view,
  forms_summernote_view,
  
  # charts
  charts_morris_view,
  charts_apex_view,
  charts_chartist_view,
  charts_chartjs_view,
  charts_flot_view,
  charts_sparkline_view,
  charts_knob_view,
 
  # maps
  maps_google_view,
  maps_vector_view,
  
  # layouts
  layouts_horizontal,
  layouts_dark_sidebar,
  layouts_small_sidebar,
  layouts_icon_sidebar,
  layouts_colored_sidebar,
  layouts_boxed_sidebar,
    
)

app_name = "components"

urlpatterns = [
    
    
  # bootstrap-ui
  path('bootstrap_ui/alerts',view=bootstrap_ui_alerts_view,name="bootstrap-ui.alerts"),
  path('bootstrap_ui/badges',view=bootstrap_ui_badges_view,name="bootstrap-ui.badges"),
  path('bootstrap_ui/buttons',view=bootstrap_ui_buttons_view,name="bootstrap-ui.buttons"),
  path('bootstrap_ui/cards',view=bootstrap_ui_cards_view,name="bootstrap-ui.cards"),
  path('bootstrap_ui/dropdowns',view=bootstrap_ui_dropdowns_view,name="bootstrap-ui.dropdowns"),
  path('bootstrap_ui/navs',view=bootstrap_ui_navs_view,name="bootstrap-ui.navs"),
  path('bootstrap_ui/tabs_accordions',view=bootstrap_ui_accordions_view,name="bootstrap-ui.tabs_accordions"),
  path('bootstrap_ui/modals',view=bootstrap_ui_modals_view,name="bootstrap-ui.modals"),
  path('bootstrap_ui/images',view=bootstrap_ui_images_view,name="bootstrap-ui.images"),
  path('bootstrap_ui/progress',view=bootstrap_ui_progress_view,name="bootstrap-ui.progressbars"),
  path('bootstrap_ui/pagination',view=bootstrap_ui_paginations_view,name="bootstrap-ui.pagination"),
  path('bootstrap_ui/popover_tooltips',view=bootstrap_ui_popover_view,name="bootstrap-ui.popover_tooltips"),
  path('bootstrap_ui/spinner',view=bootstrap_ui_spinner_view,name="bootstrap-ui.spinner"),
  path('bootstrap_ui/carousel',view=bootstrap_ui_carousel_view,name="bootstrap-ui.carousel"),
  path('bootstrap_ui/video',view=bootstrap_ui_video_view,name="bootstrap-ui.video"),
  path('bootstrap_ui/typography',bootstrap_ui_typography_view,name="bootstrap-ui.typography"),
  path('bootstrap_ui/grid',view=bootstrap_ui_grid_view,name="bootstrap-ui.grid"),

  # advance-ui
  path('advance-ui/alertify',view=advance_ui_alertify_view,name="advance-ui.alertify"),
  path('advance-ui/ratings',view=advance_ui_ratings_view,name="advance-ui.ratings"),
  path('advance-ui/nestable',view=advance_ui_nestable_view,name="advance-ui.nestable"),
  path('advance-ui/rangeslider',view=advance_ui_rangeslider_view,name="advance-ui.rangeslider"),
  path('advance-ui/sweet_alert',view=advance_ui_sweet_alert_view,name="advance-ui.sweet_alert"),
  path('advance-ui/lightbox',view=advance_ui_lightbox_view,name="advance-ui.lightbox"),
 
  # icons
  path('icons/materialdesign',view=icons_materialdesign_view,name="icons.materialdesign"),
  path('icons/dripicons',view=icons_dripicons_view,name="icons.dripicons"),
  path('icons/fontawesome',view=icons_fontawesome_view,name="icons.fontawesome"),
  path('icons/themify',view=icons_themify_view,name="icons.themify"),
  path('icons/unicons',view=icons_unicons_view,name="icons.unicons"),

  # tables
  path('tables/basic',view=tables_basic_view,name="tables.basic"),
  path('tables/datatable',view=tables_datatable_view,name="tables.datatable"),
  path('tables/responsive',view=tables_responsive_view,name="tables.responsive"),
  path('tables/editable',view=tables_editable_view,name="tables.editable"),

  # forms
  path('forms/elements',view=forms_elements_view,name="forms.elements"),
  path('forms/validation',view=forms_validation_view,name="forms.validation"),
  path('forms/advanced',view=forms_advanced_view,name="forms.advanced"),
  path('forms/editors',view=forms_editors_view,name="forms.editors"),
  path('forms/file_uploads',view=forms_file_uploads_view,name="forms.file_uploads"),
  path('forms/mask',view=forms_mask_view,name="forms.mask"),
  path('forms/summernote',view=forms_summernote_view,name="forms.summernote"),

  #  charts
  path('charts/morris',view=charts_morris_view,name="charts.morris"),
  path('charts/apex',view=charts_apex_view,name="charts.apex"),
  path('charts/chartist',view=charts_chartist_view,name="charts.chartist"),
  path('charts/chartjs',view=charts_chartjs_view,name="charts.chartjs"),
  path('charts/flot',view=charts_flot_view,name="charts.flot"),
  path('charts/sparkline',view=charts_sparkline_view,name="charts.sparkline"),
  path('charts/knob',view=charts_knob_view,name="charts.knob"),

  # maps
  path('maps/google',view=maps_google_view,name="maps.google"),
  path('maps/vector',view=maps_vector_view,name="maps.vector"),

  # layouts
  path('layouts/horizontal',view=layouts_horizontal,name="layouts.horizontal"),
  path('layouts/dark_sidebar',view=layouts_dark_sidebar,name="layouts.dark_sidebar"),
  path('layouts/small_sidebar',view=layouts_small_sidebar,name="layouts.small_sidebar"),
  path('layouts/icon_sidebar',view=layouts_icon_sidebar,name="layouts.icon_sidebar"),
  path('layouts/colored_sidebar',view=layouts_colored_sidebar,name="layouts.colored_sidebar"),
  path('layouts/boxed_sidebar',view=layouts_boxed_sidebar,name="layouts.boxed_sidebar"),

]
