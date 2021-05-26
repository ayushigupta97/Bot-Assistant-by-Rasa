

<!--## happy_path
* greet
    - find_facility_types
* inform{"facility_type": "rbry-mqwu"}    
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": 4245}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_goodbye

## happy_path_multi_requests
* greet
    - find_facility_types
* inform{"facility_type": "rbry-mqwu"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": "747604"}
    - find_healthcare_address
    - utter_address
* search_provider{"facility_type": "rbry-mqwu"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": 4245}   
    - find_healthcare_address
    - utter_address

## happy_path2
* search_provider{"location": "Austin", "facility_type": "rbry-mqwu"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": "450871"}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_goodbye-->

## happy path
* greet
  - utter_greet
  - utter_how_can_i_help
* solve
  - action_ask_technology
* issue_part
  - utter_exact_topic
  - action_give_tutorial
  - action_give_expert
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

