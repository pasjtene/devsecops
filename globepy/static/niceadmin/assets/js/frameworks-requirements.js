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
        $('.requirement-description-head').click(function(e){
          
            $(this).closest('.requirement-description').find(".requirement-details").slideToggle( "slow" );
            
        });

        $('.create-compliance-item').click(function(e){
          
            $(this).closest('.requirement-description-head11').find(".requirement-details").slideToggle( "slow" );
            
        });

        $('.edit-compliance-status').click(function(e){
          
            $(this).closest('.requirement-details').find(".editable").Toggle( "slow" );
            
        });

        

    }
   

  })();