FROM postgres:9.5
# The default value of ENV is dev
ARG ENV=dev

# Copy the sample data to the root directory
ADD ./sample_data/sample.sql /

# If arg ENV is dev, load sample data
RUN if [ "$ENV" = "dev" ] ; then \
    cp /sample.sql /docker-entrypoint-initdb.d; \
    else \
    echo The evironment is not dev; \
    fi

