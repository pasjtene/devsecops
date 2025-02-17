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
            var updateUrl = $(this).data('update-url');
            //var updateUrl = "{% url 'update_comment' 0 %}".replace("0", commentId);
            var updtext = $(this).siblings('.card-text').text();
            $('#update-comment-text').val(updtext);

                $('#update-comment-form').attr('action', updateUrl);
                $('#updateCommentModal').modal('show');

        });

         // Handle delete comment modal
         $('.delete-btn').click(function(e) {
            e.preventDefault();
            var commentId = $(this).data('comment-id');
            var deleteUrl = $(this).data('delete-url');
            //var updateUrl = "{% url 'update_comment' 0 %}".replace("0", commentId);
            var deltext = $(this).siblings('.card-text').text();
            $('#delete-comment-text').val(deltext);

                $('#delete-comment-form').attr('action', deleteUrl);
                $('#deleteCommentModal').modal('show');

        });


         // Handle delete comment via AJAX
         $('#delete-comment-form').submit(function(e) {
            e.preventDefault();
            var form = $(this);
            var url = form.attr('action');
            var commentText = $('#delete-comment-text').val();
            $('#deleteCommentModal').modal('hide');

            $.ajax({
                url: url,
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                    'comment_text': commentText
                },
                success: function(response) {
                    if (response.success) {
                        
                        $('#'+response.comment_id).remove();
                        $('.ajax-alert').show()
                        $('.alert-dismissible').show()
                        $('#ajax-alert-message').text("Comment deleted successfuly ");
                      
                    } else {
                        alert('Error updating comment.');
                    }
                },
                error: function(response) {
                    alert('Error updating comment.');
                }
            });
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

    });

    }

  })();