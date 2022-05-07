-- upgrade --
ALTER TABLE "user" ADD "last_name" TEXT;
ALTER TABLE "user" ADD "first_name" TEXT;
ALTER TABLE "user" ALTER COLUMN "created_at" SET NOT NULL;
ALTER TABLE "user" ALTER COLUMN "updated_at" SET NOT NULL;
-- downgrade --
ALTER TABLE "user" DROP COLUMN "last_name";
ALTER TABLE "user" DROP COLUMN "first_name";
ALTER TABLE "user" ALTER COLUMN "created_at" DROP NOT NULL;
ALTER TABLE "user" ALTER COLUMN "updated_at" DROP NOT NULL;
