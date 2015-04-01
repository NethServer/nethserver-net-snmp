<?php

/* @var $view Nethgui\Renderer\Xhtml */

echo $view->header()->setAttribute('template', $T('Snmp_header'));

echo $view->fieldset()->setAttribute('template', $T('status_label'))
  ->insert($view->radioButton('status', 'disabled'))

  ->insert($view->fieldsetSwitch('status', 'enabled', $view::FIELDSETSWITCH_EXPANDABLE)
    ->insert($view->textInput('Community'))
    ->insert($view->textInput('SysContact'))
    ->insert($view->textInput('SysLocation')))
;

echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_HELP);
