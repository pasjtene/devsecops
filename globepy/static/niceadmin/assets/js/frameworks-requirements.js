/**
* Created: 2025/02/11
* 
* Updated: Apr 20 2024 with Bootstrap v5.3.3
* Author: Pascal Tene
* License: To be confirmed (Private)
*/

(function() {
    "use strict";
    viewRequirementDetails();
    addComment();
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
          
            $(this).closest('.requirement-details').find(".editable").toggle();
            $(this).closest('.requirement-details').find(".non-editable").toggle();
            
        });

    }


    function addComment() {
       
    $(document).ready(function() {
        // Toggle comment form
        $('#add-comment-btn').click(function() {
            $('#comment-form').toggle();
        });

        // Toggle reply form for each comment
        $('.reply-btn').click(function() {
            var replyForm = $(this).siblings('.reply-form');
            replyForm.toggle();
        });
    });

    }

  })();