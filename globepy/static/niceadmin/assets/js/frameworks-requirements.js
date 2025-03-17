/**
* Created: 2025/02/11
* 
* Updated: Apr 20 2024 with Bootstrap v5.3.3
* Author: Pascal Tene
* License: To be confirmed (Private)
*/

(function() {
    "use strict";
    


   
       
    $(document).ready(function() {
       

        viewRequirementDetails();
        Comment();
        //addComment();
        /**
         * Easy selector helper function
         */
       
        function viewRequirementDetails() {
            $('.requirement-description-head').click(function(e){
              
                $(this).closest('.requirement-description').find(".requirement-details").slideToggle( "slow" );
                
            });
    
            $('.create-compliance-item').click(function(e){
              
                $(this).closest('.requirement-description-head11').find(".requirement-details").slideToggle( "slow" );
                console.log("Create compliance item clicked");
                
            });
    
            $('.edit-compliance-status').click(function(e){
              
                $(this).closest('.requirement-details').find(".editable").toggle();
                $(this).closest('.requirement-details').find(".non-editable").toggle();
                
            });
    
        }


        function Comment() {
            // Toggle comment form
            $('#add-comment-btn').click(function() {
              $('#comment-form').toggle();
          });
      
          // Toggle reply form for each comment
          $('.reply-btn').click(function() {
              var replyForm = $(this).siblings('.reply-form');
              replyForm.toggle();
          });
      
      
              // Handle form submission via AJAX
              $('#update-comment-form').submit(function(e) {
                  e.preventDefault();
                  var form = $(this);
                  var url = form.attr('action');
                  var commentText = $('#update-comment-text').val();
                  $('#updateCommentModal').modal('hide');
      
                  $.ajax({
                      url: url,
                      type: 'POST',
                      data: {
                          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                          'comment_text': commentText
                      },
                      success: function(response) {
                          if (response.success) {
                              
                              $('#text'+response.comment_id).text(response.comment_text);
                              $('.ajax-alert').show()
                              $('.alert-dismissible').show()
                              $('#ajax-alert-message').text("Comment updated successfuly ");
                             
                          } else {
                              alert('Error updating comment.');
                          }
                      },
                      error: function(response) {
                          alert('Error updating comment.');
                      }
                  });
              });
      
      
         }

            

    });

   

  })();