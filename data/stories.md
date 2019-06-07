## story_greet
* greet
 - utter_greet
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_what_can_you_do_02
* greet
 - utter_greet
* what_can_you_do
 - utter_what_can_you_do
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye

## story_details
* details{"code":"c12390"}
 - slot{"code":"c12390"}
 - action_details
 - slot{"code":"12390"}
 
## story_details_01
* what_can_you_do
 - utter_what_can_you_do
* details{"code":"c12390"}
 - slot{"code":"c12390"}
 - action_details
 - slot{"code":"12390"}
* details{"code":"c23941"}
 - slot{"code":"c23941"}
 - action_details
 - slot{"code":"23941"}
 
## story_details_02
* greet
 - utter_greet
* details{"name":"bachelor of science in it"}
 - action_details
 - slot{"code":"10148"}
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
 
## story_details_03
* greet
 - utter_greet
* what_can_you_do
 - utter_what_can_you_do
* details{"code":"c12932"}
 - slot{"code":"c12932"}
 - action_details
 - slot{"code":"12932"}
* goodbye
 - utter_goodbye 
 
## story_details_04
* greet
 - utter_greet
* details{"code":"31251"}
 - slot{"code":"31251"}
 - action_details
 - slot{"code":"31251"}
* goodbye
 - utter_goodbye 
 
## story_children_01
* greet
    - utter_greet
* details{"code":"41004"}
    - slot{"code":"41004"}
    - action_details
    - slot{"code":"41004"}
* children
    - action_children
    - slot{"code":"41004"}
* children{"code": "c10219"}
    - slot{"code": "c10219"}
    - action_children
    - slot{"code":"10219"}
 
## story_children_01
* details{"code":"c12390"}
 - slot{"code":"c12390"}
 - action_details
 - slot{"code":"12390"}
* children
 - action_children
 - slot{"code":"12390"}
 
## story_children_02
* greet
 - utter_greet
* details{"name":"bachelor in business bachelor of science in it"}
 - action_details
 - slot{"code":"10219"}
* children
 - action_children
 - slot{"code":"10219"}
* goodbye
 - utter_goodbye 
 
## story_children_03
* greet
 - utter_greet
* what_can_you_do
 - utter_what_can_you_do
* children{"code":"c12932"}
 - slot{"code":"c12932"}
 - action_children
 - slot{"code":"12932"}
* goodbye
 - utter_goodbye 
 
## story_children_04
* greet
 - utter_greet
* children{"code":"c10219"}
 - slot{"code":"c10219"}
 - action_children
 - slot{"code":"10219"}
* details{"code":"31241"}
 - slot{"code":"31241"}
 - action_details
 - slot{"code":"31241"}
* goodbye
 - utter_goodbye 
 - utter_goodbye 

## story_hons
* greet
 - utter_greet
* honours{"code":"c10148"}
 - slot{"code":"c10148"}
 - action_hons
 - slot{"code":"10148"}
* details
 - action_details
 - slot{"code":"10148"}
* thanks
 - utter_thanks
 
## story_hons_01
* greet
 - utter_greet
* honours{"code":"c23467"}
 - slot{"code":"c23467"}
 - action_hons
 - slot{"code":"23467"}

## story_prof_prac
* greet
 - utter_greet
* prof_prac{"code":"c10148"}
 - slot{"code":"c10148"}
 - action_prof_prac
 - slot{"code":"10148"}
* details
 - action_details
 - slot{"code":"10148"}
* thanks
 - utter_thanks
 
## story_prof_prac_01
* greet
 - utter_greet
* prof_prac{"code":"c23467"} 
 - slot{"code":"c23467"}
 - action_prof_prac
 - slot{"code":"23467"}
 
## story_combined
* greet
 - utter_greet{"code":"c10148"}
* details
 - slot{"code":"c10148"}
 - action_details
 - slot{"code":"10148"}
* combined
 - slot{"code":"c10148"}
 - action_combined
 - slot{"code":"10148"}
* thanks
 - utter_thanks
    
## story_combined_01
* greet
 - utter_greet
* combined{"code":"c23467"}
 - slot{"code":"c23467"}
 - action_combined