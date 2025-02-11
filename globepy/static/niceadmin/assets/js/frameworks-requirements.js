/**
* Created: 2025/02/11
* 
* Updated: Apr 20 2024 with Bootstrap v5.3.3
* Author: Pascal Tene
* License: To be confirmed (Private)
*/

(function() {
    "use strict";
    viewRequirementDetails() 
    /**
     * Easy selector helper function
     */
   
    function viewRequirementDetails() {
        $('.requirement-description').click(function(e){
            
            console.log("Requirement clicked...!")
            
            $(this).closest('.requirement-details').show();
            $(this).closest('.requirement-details').find(".activity-edit").show();
            
        });
    
       
    }
   

  })();