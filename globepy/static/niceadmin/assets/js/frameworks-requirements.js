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

  
        // Handle update comment modal
        $('.update-btn').click(function(e) {
            e.preventDefault();
            var commentId = $(this).data('comment-id');
            var updateUrl = "{% url 'update_comment' 0 %}".replace("0", commentId);

                $('#update-comment-form').attr('action', updateUrl);
                $('#updateCommentModal').modal('show');

                console.log("The url is ",updateUrl);
            
            // Fetch the current comment text
            $.get(updateUrl, function(data) {
                $('#update-comment-text').val(data.comment_text);
                $('#update-comment-form').attr('action', updateUrl);
                $('#updateCommentModal').modal('show');
            });
        });


            // Handle form submission via AJAX
            $('#update-comment-form').submit(function(e) {
                e.preventDefault();
                var form = $(this);
                var url = form.attr('action');
                var commentText = $('#update-comment-text').val();

                $.ajax({
                    url: url,
                    type: 'POST',
                    data: {
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                        'comment_text': commentText
                    },
                    success: function(response) {
                        if (response.success) {
                            $('#updateCommentModal').modal('hide');
                            location.reload(); // Reload the page to reflect changes
                        } else {
                            alert('Error updating comment.');
                        }
                    },
                    error: function(response) {
                        alert('Error updating comment.');
                    }
                });
            });




    });

    }

  })();